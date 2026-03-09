import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ── CONFIG ──────────────────────────────────────────────────────────────────
# CSV_PATH = r'C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\boutside_corner_1\boutside_corner_1_0.db\scan.csv'
CSV_PATH = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\base_case\base_case_0.db\scan.csv"
SIDE = 1          # 1 = left wall, -1 = right wall
VELOCITY = 1.0
DESIRED_DISTANCE = 1.0
# ────────────────────────────────────────────────────────────────────────────


STEER_CSV = r'C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\base_case\base_case_0.db\vesc\low_level\ackermann_cmd.csv'
df_steer = pd.read_csv(STEER_CSV).sort_values('time').reset_index(drop=True)

def compute_error(row, side, velocity, desired_distance):
    """Replicates the slice_scan logic from bag_grapher.py"""
    
    # Pull ranges from the row
    range_cols = [f'ranges_{i}' for i in range(1081)]
    ranges = row[range_cols].values.astype(float)

    range_min = row['range_min']
    range_max = row['range_max']
    angle_min = row['angle_min']
    angle_max = row['angle_max']

    # Reconstruct angles
    all_angles = np.linspace(angle_min, angle_max, len(ranges))

    # Valid range mask
    valid_mask = (ranges > range_min) & (ranges < range_max)

    # Side mask (left or right wall)
    if side == 1:
        wall_mask = valid_mask & (all_angles > (np.pi / 3.0)) & (all_angles < (115.0 * np.pi / 180.0))
    else:
        wall_mask = valid_mask & (all_angles < -(np.pi / 3.0)) & (all_angles > -(115.0 * np.pi / 180.0))

    wall_distances = ranges[wall_mask]
    needed_angles  = all_angles[wall_mask]

    # Convert to cartesian
    all_x = wall_distances * np.cos(needed_angles)
    all_y = wall_distances * np.sin(needed_angles)

    # Outlier removal via median
    if len(all_y) == 0:
        return 0.0

    median_y  = np.median(all_y)
    tolerance = 0.4
    good_mask = np.abs(all_y - median_y) < tolerance
    good_x    = all_x[good_mask]
    good_y    = all_y[good_mask]

    # Edge cases
    if len(good_x) < 2:
        return float(0.34 * side)

    if np.ptp(good_x) < 0.1:
        return 0.0

    # Linear regression → predicted wall distance
    m, c = np.polyfit(good_x, good_y, 1)
    x_offset    = velocity * 0.5
    y_at_offset = (m * x_offset) + c

    # Front wall emergency detection
    front_mask   = valid_mask & (all_angles > -0.2) & (all_angles < 0.2)
    front_ranges = ranges[front_mask]

    front_error = 0.0
    if len(front_ranges) > 0:
        front_dist = np.min(front_ranges)
        safe_dist  = desired_distance * velocity
        if front_dist < safe_dist:
            front_error = (safe_dist - front_dist) * 2.0

    error = desired_distance - abs(y_at_offset) + front_error
    # percent_error = abs(exp_error / desired_distance)  * 100.0

    return error


# ── LOAD DATA ────────────────────────────────────────────────────────────────
print("Loading CSV...")
# df = pd.read_csv(CSV_PATH, sep=',t')  # change sep=',' if comma-separated
df = pd.read_csv(CSV_PATH)  # default sep=','
df = df.sort_values('time').reset_index(drop=True)

# Then convert timestamps as before
timestamps = pd.to_datetime(df['time']).astype('int64') / 1e9
t0         = timestamps.iloc[0]
time_secs  = (timestamps - t0).values


# ── COMPUTE ERROR FOR EVERY ROW ───────────────────────────────────────────────
print("Computing error...")
errors = []
for _, row in df.iterrows():
    e = (abs(compute_error(row, SIDE, VELOCITY, DESIRED_DISTANCE))/DESIRED_DISTANCE) *100
    errors.append(e)

errors = np.array(errors)

# Set your desired start time (in seconds relative to t0)
START_TIME = 55  # e.g. skip the first 30 seconds

# Trim both arrays
mask              = time_secs >= START_TIME
time_secs_trimmed = time_secs[mask]
errors_trimmed    = errors[mask]

steer_timestamps = pd.to_datetime(df_steer['time']).astype('int64') / 1e9
steer_time_secs  = (steer_timestamps - t0).values  # use same t0 as scan

# Trim to same start time
steer_mask       = steer_time_secs >= START_TIME
steer_time_trimmed  = steer_time_secs[steer_mask]
steering_trimmed = df_steer['drive_steering_angle'][steer_mask].values  # adjust column name

fig, ax1 = plt.subplots(figsize=(14, 6))

# ── Plot 1: Error on left y-axis ──
color_error = 'steelblue'
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Error (% of desired distance)', color=color_error)
ax1.plot(time_secs_trimmed, errors_trimmed, color=color_error, linewidth=1.2, label='Error')
ax1.axhline(0, color=color_error, linestyle='--', linewidth=0.8, alpha=0.5)
ax1.tick_params(axis='y', labelcolor=color_error)
ax1.grid(True, alpha=0.3)

# ── Plot 2: Steering angle on right y-axis ──
ax2 = ax1.twinx()  # shares the same x-axis
color_steer = 'darkorange'
ax2.set_ylabel('Steering Angle (rad)', color=color_steer)
ax2.plot(steer_time_trimmed, steering_trimmed, color=color_steer, linewidth=1.2, label='Steering Angle')
ax2.tick_params(axis='y', labelcolor=color_steer)

# ── Align both y-axes so 0 is at the same position ──
ax1_ylim = ax1.get_ylim()
ax2_ylim = ax2.get_ylim()

# Find the largest range needed on each side of 0
ax1_max = max(abs(ax1_ylim[0]), abs(ax1_ylim[1]))
ax2_max = max(abs(ax2_ylim[0]), abs(ax2_ylim[1]))

# Set both axes to be symmetric around 0
ax1.set_ylim(-ax1_max, ax1_max)
ax2.set_ylim(-ax2_max, ax2_max)

# ── Combined legend ──
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.title('Error % vs Steering Angle over Time')
plt.tight_layout()
plt.savefig('error_vs_steering.png', dpi=150)
plt.show()


# # ── PLOT ──────────────────────────────────────────────────────────────────────
# fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# # Error over time
# axes[0].plot(time_secs_trimmed, errors_trimmed, color='steelblue', linewidth=1.2)
# axes[0].axhline(0, color='red', linestyle='--', linewidth=1, label='Zero error')
# axes[0].set_ylabel('Error (m)')
# axes[0].set_title('Wall Following Error for Base Case over Time')
# axes[0].legend()
# axes[0].grid(True, alpha=0.3)

# # Absolute error
# axes[1].plot(time_secs_trimmed, np.abs(errors_trimmed), color='darkorange', linewidth=1.2)
# axes[1].set_ylabel('|Error| (m)')
# axes[1].set_xlabel('Time (s)')
# axes[1].set_title('Absolute Error for Base Case over Time')
# axes[1].grid(True, alpha=0.3)

# plt.tight_layout()
# plt.savefig('base_case0_error_plot.png', dpi=150)
# plt.show()

print(f"\nStats:")
print(f"  Mean error:     {np.mean(errors):.4f} m")
print(f"  Mean |error|:   {np.mean(np.abs(errors)):.4f} m")
print(f"  Max |error|:    {np.max(np.abs(errors)):.4f} m")
print(f"  Std dev:        {np.std(errors):.4f} m")