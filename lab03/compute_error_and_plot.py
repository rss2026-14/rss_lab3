import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
# straigh v1 vs v2:
trial11 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_1_speed_1\straight_1_speed_1_0.db\scan.csv"
trial12 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_2_speed_1\straight_2_speed_1_0.db\scan.csv"
trial13 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_23_speed_1\straight_23_speed_1_0.db\scan.csv"

trial21 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\ostraight_1_speed_2\ostraight_1_speed_2_0.db\scan.csv"
trial22 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_2_speed_2\straight_2_speed_2_0.db\scan.csv"
trial23 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straighht_3_speed_2\straighht_3_speed_2_0.db\scan.csv"


# # inside corner turn speed1
# trial11 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_1_speed_1\sinside_corner_1_speed_1_0.db\scan.csv"
# trial12 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_2_speed_1\sinside_corner_2_speed_1_0.db\scan.csv"
# trial13 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_23_speed_1\sinside_corner_23_speed_1_0.db\scan.csv"

# # inside corner turn speed2
# trial21 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_1_speed_2\sinside_corner_1_speed_2_0.db\scan.csv"
# trial22 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_12_speed_2\sinside_corner_12_speed_2_0.db\scan.csv"
# trial23 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_23_speed_1\sinside_corner_23_speed_1_0.db\scan.csv"

# outside corner turn speed1
trial11 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout_1_speed_1\sout_1_speed_1_0.db\scan.csv"
trial12 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout_2_speed_1\sout_2_speed_1_0.db\scan.csv"
trial13 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout_23_speed_1\sout_23_speed_1_0.db\scan.csv"

#outside corner turn speed2
trial21 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout_1_speed_2\sout_1_speed_2_0.db\scan.csv"
trial22 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\out_2_speed_2\out_2_speed_2_0.db\scan.csv"
trial23 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\outt_3_speed_2\outt_3_speed_2_0.db\scan.csv"


# # straight 45 degrees inward speed1
# trial11 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\in45_1_speed_1\in45_1_speed_1_0.db\scan.csv"
# trial12 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\in45_12_speed_1\in45_12_speed_1_0.db\scan.csv"
# trial13 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\in45_13_speed_1\in45_13_speed_1_0.db\scan.csv"

# # straight 45 degrees inward speed2
# trial21 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\in45_1_speed_2\in45_1_speed_2_0.db\scan.csv"
# trial23 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sin45_3_speed_2\sin45_3_speed_2_0.db\scan.csv"

# #straight 45 degrees outward speed1
# trial11 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\iout45_1_speed_1\iout45_1_speed_1_0.db\scan.csv"
# trial12 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\iout45_2_speed_1\iout45_2_speed_1_0.db\scan.csv"
# trial13 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\iout45_3_speed_1\iout45_3_speed_1_0.db\scan.csv"

# # straight 45 degrees outward speed2
# trial21 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout45_1_speed_2\sout45_1_speed_2_0.db\scan.csv"
# trial22 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout45_12_speed_2\sout45_12_speed_2_0.db\scan.csv"
# trial23 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout45_3_speed_2\sout45_3_speed_2_0.db\scan.csv"



# ── CONFIG ───────────────────────────────────────────────────────────────────
VELOCITY_1_TRIALS = [
    {'path': trial11, 'label': 'V1 Trial 1'},
    {'path': trial12, 'label': 'V1 Trial 2'},
    {'path': trial13, 'label': 'V1 Trial 3'},
]

VELOCITY_2_TRIALS = [
    {'path': trial21, 'label': 'V2 Trial 1'},
    {'path': trial22, 'label': 'V2 Trial 2'},
    {'path': trial23, 'label': 'V2 Trial 3'},
]


# ── CONFIG ───────────────────────────────────────────────────────────────────

SIDE             = 1
DESIRED_DISTANCE = 1.0
CLIP_TIME        = 9.0   # seconds to show per trial
TRIAL_STARTS     = {     # per-trial start times
    'v1': [9,4.5,7.1],  # start times for each velocity 1 trial
    'v2': [2.15,3.9,3.1],  # start times for each velocity 2 trial
}
# ─────────────────────────────────────────────────────────────────────────────

def compute_error(row, side, velocity, desired_distance):
    range_cols = [f'ranges_{i}' for i in range(1081)]
    ranges = row[range_cols].values.astype(float)

    range_min = row['range_min']
    range_max = row['range_max']
    angle_min = row['angle_min']
    angle_max = row['angle_max']

    all_angles = np.linspace(angle_min, angle_max, len(ranges))
    valid_mask = (ranges > range_min) & (ranges < range_max)

    if side == 1:
        wall_mask = valid_mask & (all_angles > (np.pi / 3.0)) & (all_angles < (115.0 * np.pi / 180.0))
    else:
        wall_mask = valid_mask & (all_angles < -(np.pi / 3.0)) & (all_angles > -(115.0 * np.pi / 180.0))

    wall_distances = ranges[wall_mask]
    needed_angles  = all_angles[wall_mask]

    all_x = wall_distances * np.cos(needed_angles)
    all_y = wall_distances * np.sin(needed_angles)

    if len(all_y) == 0:
        return 0.0

    median_y  = np.median(all_y)
    tolerance = 0.4
    good_mask = np.abs(all_y - median_y) < tolerance
    good_x    = all_x[good_mask]
    good_y    = all_y[good_mask]

    if len(good_x) < 2:
        return float(0.34 * side)
    if np.ptp(good_x) < 0.1:
        return 0.0

    m, c        = np.polyfit(good_x, good_y, 1)
    x_offset    = velocity * 0.5
    y_at_offset = (m * x_offset) + c

    front_mask   = valid_mask & (all_angles > -0.2) & (all_angles < 0.2)
    front_ranges = ranges[front_mask]

    front_error = 0.0
    if len(front_ranges) > 0:
        front_dist = np.min(front_ranges)
        safe_dist  = desired_distance * velocity
        if front_dist < safe_dist:
            front_error = (safe_dist - front_dist) * 2.0

    return desired_distance - abs(y_at_offset) + front_error


def load_trial_errors(trials, starts, velocity):
    """Load and process errors for a set of trials, returns list of (time, error) arrays."""
    all_errors = []

    for trial, start in zip(trials, starts):
        df = pd.read_csv(trial['path']).sort_values('time').reset_index(drop=True)

        timestamps = pd.to_datetime(df['time']).astype('int64') / 1e9
        t0         = timestamps.iloc[0]
        time_secs  = (timestamps - t0).values

        errors = np.array([compute_error(row, SIDE, velocity, DESIRED_DISTANCE)
                           for _, row in df.iterrows()])

        # Trim start
        mask      = time_secs >= start
        if mask.sum() == 0:
            print(f"Warning: start_time {start}s exceeds trial duration {time_secs[-1]:.1f}s for {trial['path']}. Using full trial.")
            mask = np.ones(len(time_secs), dtype=bool)
        time_trim = time_secs[mask] - time_secs[mask][0]
        err_trim  = (errors[mask]/DESIRED_DISTANCE) *100
        # err_trim = errors[mask]
        # # Clip to 9 seconds
        clip_mask = time_trim <= 6.25
        time_trim = time_trim[clip_mask]
        err_trim  = err_trim[clip_mask]

        all_errors.append((time_trim, err_trim))

    return all_errors


def average_errors(trial_errors):
    """Interpolate all trials onto a common time axis and average them."""
    # Common time axis at 100Hz resolution
    common_time = np.linspace(0, CLIP_TIME, 900)

    interpolated = []
    for time_trim, err_trim in trial_errors:
        interp = np.interp(common_time, time_trim, err_trim)
        interpolated.append(interp)

    avg_error = np.mean(interpolated, axis=0)
    std_error = np.std(interpolated, axis=0)

    return common_time, avg_error, std_error


# ── LOAD & AVERAGE ────────────────────────────────────────────────────────────
print("Processing velocity 1 trials...")
v1_trial_errors          = load_trial_errors(VELOCITY_1_TRIALS, TRIAL_STARTS['v1'], velocity=1.0)
v1_time, v1_avg, v1_std  = average_errors(v1_trial_errors)

print("Processing velocity 2 trials...")
v2_trial_errors          = load_trial_errors(VELOCITY_2_TRIALS, TRIAL_STARTS['v2'], velocity=2.0)
v2_time, v2_avg, v2_std  = average_errors(v2_trial_errors)

# ── PLOT ──────────────────────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(14, 6))

# Velocity 1 — average line + shaded std deviation band
ax.plot(v1_time, v1_avg, color='olivedrab', linewidth=2.0, label='Velocity 1 - 1m/s (avg across three trials)')
ax.axhline(5, color='red', linestyle='--', linewidth=1.2, label='+5% margin')
# ax.fill_between(v1_time, v1_avg - v1_std, v1_avg + v1_std, color='steelblue', alpha=0.2, label='V1 ± std dev')

# Velocity 2 — average line + shaded std deviation band
ax.plot(v2_time, v2_avg, color='steelblue', linewidth=2.0, label='Velocity 2 - 2m/s (avg across two trials)')
ax.axhline(-5, color='red', linestyle='--', linewidth=1.2, label='-5% margin')
# ax.fill_between(v2_time, v2_avg - v2_std, v2_avg + v2_std, color='darkorange', alpha=0.2, label='V2 ± std dev')
ax.set_ylim(-100,100)
ax.set_xlim(0,8)

ax.set_xlabel('Time (s)')
ax.set_ylabel('% Error (error/desired distance * 100)')
ax.set_title('Average Wall Following Error Across Three Trials for Straight Path — Velocity 1 vs Velocity 2')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('straight_avg_error_v1_vs_v2.png', dpi=150)
plt.show()


# ── STATS ─────────────────────────────────────────────────────────────────────
print("\n── Velocity 1 ──")
print(f"  Max error:  {v1_avg.max():.2f}%")
print(f"  Min error:  {v1_avg.min():.2f}%")
print(f"  Avg error:  {v1_avg.mean():.2f}%")

print("\n── Velocity 2 ──")
print(f"  Max error:  {v2_avg.max():.2f}%")
print(f"  Min error:  {v2_avg.min():.2f}%")
print(f"  Avg error:  {v2_avg.mean():.2f}%")





# #to showcase that our wall following algorithm is 
# #working and has a very small error over time. 
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# trial11 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_1_speed_1\straight_1_speed_1_0.db\scan.csv"
# trial12 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_2_speed_1\straight_2_speed_1_0.db\scan.csv"
# trial13 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_23_speed_1\straight_23_speed_1_0.db\scan.csv"


# trial21 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\ostraight_1_speed_2\ostraight_1_speed_2_0.db\scan.csv"
# trial22 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_2_speed_2\straight_2_speed_2_0.db\scan.csv"
# trial23 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straighht_3_speed_2\straighht_3_speed_2_0.db\scan.csv"


# # ── CONFIG ───────────────────────────────────────────────────────────────────
# # TRIALS = [
# #     {'path': trial1, 'label': 'Trial 1', 'start_time': 3.5},
# #     {'path': trial2, 'label': 'Trial 2', 'start_time': 5.5},
# #     {'path': trial3, 'label': 'Trial 3', 'start_time': 6.1},
# # ]

# VELOCITY_1_TRIALS = [
#     {'path': trial11 'label': 'V1 Trial 1'},
#     {'path': trial12, 'label': 'V1 Trial 2'},
#     {'path': trial13, 'label': 'V1 Trial 3'},
# ]

# VELOCITY_2_TRIALS = [
#     {'path': trial21, 'label': 'V2 Trial 1'},
#     {'path': trial22, 'label': 'V2 Trial 2'},
#     {'path': trial23, 'label': 'V2 Trial 3'},
# ]


# SIDE             = 1
# VELOCITY         = 1.0
# DESIRED_DISTANCE = 1.0
# # START_TIME       = 0  # seconds to trim from start
# # ─────────────────────────────────────────────────────────────────────────────

# def compute_error(row, side, velocity, desired_distance):
#     """Replicates the slice_scan logic from bag_grapher.py"""
    
#     # Pull ranges from the row
#     range_cols = [f'ranges_{i}' for i in range(1081)]
#     ranges = row[range_cols].values.astype(float)

#     range_min = row['range_min']
#     range_max = row['range_max']
#     angle_min = row['angle_min']
#     angle_max = row['angle_max']

#     # Reconstruct angles
#     all_angles = np.linspace(angle_min, angle_max, len(ranges))

#     # Valid range mask
#     valid_mask = (ranges > range_min) & (ranges < range_max)

#     # Side mask (left or right wall)
#     if side == 1:
#         wall_mask = valid_mask & (all_angles > (np.pi / 3.0)) & (all_angles < (115.0 * np.pi / 180.0))
#     else:
#         wall_mask = valid_mask & (all_angles < -(np.pi / 3.0)) & (all_angles > -(115.0 * np.pi / 180.0))

#     wall_distances = ranges[wall_mask]
#     needed_angles  = all_angles[wall_mask]

#     # Convert to cartesian
#     all_x = wall_distances * np.cos(needed_angles)
#     all_y = wall_distances * np.sin(needed_angles)

#     # Outlier removal via median
#     if len(all_y) == 0:
#         return 0.0

#     median_y  = np.median(all_y)
#     tolerance = 0.4
#     good_mask = np.abs(all_y - median_y) < tolerance
#     good_x    = all_x[good_mask]
#     good_y    = all_y[good_mask]

#     # Edge cases
#     if len(good_x) < 2:
#         return float(0.34 * side)

#     if np.ptp(good_x) < 0.1:
#         return 0.0

#     # Linear regression → predicted wall distance
#     m, c = np.polyfit(good_x, good_y, 1)
#     x_offset    = velocity * 0.5
#     y_at_offset = (m * x_offset) + c

#     # Front wall emergency detection
#     front_mask   = valid_mask & (all_angles > -0.2) & (all_angles < 0.2)
#     front_ranges = ranges[front_mask]

#     front_error = 0.0
#     if len(front_ranges) > 0:
#         front_dist = np.min(front_ranges)
#         safe_dist  = desired_distance * velocity
#         if front_dist < safe_dist:
#             front_error = (safe_dist - front_dist) * 2.0

#     error = desired_distance - abs(y_at_offset) + front_error
#     # percent_error = abs(exp_error / desired_distance)  * 100.0

#     return error

# fig, ax = plt.subplots(figsize=(14, 6))

# colors = ['lightcoral', 'darkgreen', 'cornflowerblue']

# for trial, color in zip(TRIALS, colors):
#     df = pd.read_csv(trial['path']).sort_values('time').reset_index(drop=True)

#     timestamps = pd.to_datetime(df['time']).astype('int64') / 1e9
#     t0         = timestamps.iloc[0]
#     time_secs  = (timestamps - t0).values

#     errors = np.array([compute_error(row, SIDE, VELOCITY, DESIRED_DISTANCE)
#                        for _, row in df.iterrows()])

#     errors_pct = ((np.abs(errors))/DESIRED_DISTANCE) * 100
#     start = trial['start_time']
#     mask      = time_secs >= start
#     time_trim = time_secs[mask] - time_secs[mask][0]  # re-zero to 0
#     err_trim  = errors_pct[mask]
#     # err_trim = errors[mask]

#     # # ✅ Clip to first 10.5 seconds
#     clip_mask = time_trim <= 10.5
#     time_trim = time_trim[clip_mask]
#     err_trim  = err_trim[clip_mask]

#     ax.plot(time_trim, err_trim, color=color, linewidth=1.2, label=trial['label'])

# ax.axhline(0,   color='red',  linestyle='--', linewidth=1.0, alpha=0.7, label='Zero error')
# ax.axhline(10,  color='gray', linestyle=':',  linewidth=0.8, alpha=0.5)
# ax.axhline(-10, color='gray', linestyle=':',  linewidth=0.8, alpha=0.5)
# ax.set_ylim(0,100)
# # ax.set_ylim(-2,2)

# # ax.locator_params(axis='x', nbins=3) 
# ax.set_xlabel('Time (s)')
# ax.set_ylabel('% Error (error/desired distance * 100)')
# ax.set_title('Wall-Following Algorithm - % Error over Time for "Straight Path, Velocity = 1.0 m/s" - Three Trials')
# ax.legend()
# ax.grid(True, alpha=0.3)

# plt.tight_layout()
# plt.savefig('straight_v1_3trials_errorpct.png', dpi=150)
# plt.show()

# #straight speed 1
# # trial1 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_1_speed_1\straight_1_speed_1_0.db\scan.csv"
# # trial2 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_2_speed_1\straight_2_speed_1_0.db\scan.csv"
# # trial3 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_23_speed_1\straight_23_speed_1_0.db\scan.csv"

# #straight speed 2
# # trial1 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\ostraight_1_speed_2\ostraight_1_speed_2_0.db\scan.csv"
# # trial2 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straight_2_speed_2\straight_2_speed_2_0.db\scan.csv"
# # trial3 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\straighht_3_speed_2\straighht_3_speed_2_0.db\scan.csv"

# #straight 45 degrees inward speed1
# # trial1 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\in45_1_speed_1\in45_1_speed_1_0.db\scan.csv"
# # trial2 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\in45_12_speed_1\in45_12_speed_1_0.db\scan.csv"
# # trial3 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\in45_13_speed_1\in45_13_speed_1_0.db\scan.csv"

# #straight 45 degrees inward speed2
# #trial1 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\in45_1_speed_2\in45_1_speed_2_0.db\scan.csv"
# #trial3 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sin45_3_speed_2\sin45_3_speed_2_0.db\scan.csv"

# #straight 45 degrees outward speed1
# #trial1 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\iout45_1_speed_1\iout45_1_speed_1_0.db\scan.csv"
# #trial2 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\iout45_2_speed_1\iout45_2_speed_1_0.db\scan.csv"
# #trial3 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\iout45_3_speed_1\iout45_3_speed_1_0.db\scan.csv"

# #straight 45 degrees outward speed2
# # trial1 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout45_1_speed_2\sout45_1_speed_2_0.db\scan.csv"
# # trial2 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout45_12_speed_2\sout45_12_speed_2_0.db\scan.csv"
# # trial3 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout45_3_speed_2\sout45_3_speed_2_0.db\scan.csv"

# #inside corner turn speed1
# # trial1 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_1_speed_1\sinside_corner_1_speed_1_0.db\scan.csv"
# # trial2 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_2_speed_1\sinside_corner_2_speed_1_0.db\scan.csv"
# # trial3 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_23_speed_1\sinside_corner_23_speed_1_0.db\scan.csv"

# #inside corner turn speed2
# # trial1 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_1_speed_2\sinside_corner_1_speed_2_0.db\scan.csv"
# # trial2 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_12_speed_2\sinside_corner_12_speed_2_0.db\scan.csv"
# # trial3 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sinside_corner_23_speed_1\sinside_corner_23_speed_1_0.db\scan.csv"

# # #outside corner turn speed1
# # trial1 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout_1_speed_1\sout_1_speed_1_0.db\scan.csv"
# # trial2 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout_2_speed_1\sout_2_speed_1_0.db\scan.csv"
# # trial3 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout_23_speed_1\sout_23_speed_1_0.db\scan.csv"

# # #outside corner turn speed2
# # trial1 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\sout_1_speed_2\sout_1_speed_2_0.db\scan.csv"
# # trial2 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\out_2_speed_2\out_2_speed_2_0.db\scan.csv"
# # trial3 = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\outt_3_speed_2\outt_3_speed_2_0.db\scan.csv"


# # import numpy as np
# # import pandas as pd
# # import matplotlib.pyplot as plt

# # # ── CONFIG ──────────────────────────────────────────────────────────────────
# # # CSV_PATH = r'C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\boutside_corner_1\boutside_corner_1_0.db\scan.csv'
# # CSV_PATH = r"C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\base_case\base_case_0.db\scan.csv"
# # SIDE = 1          # 1 = left wall, -1 = right wall
# # VELOCITY = 1.0
# # DESIRED_DISTANCE = 1.0
# # # ────────────────────────────────────────────────────────────────────────────

# # STEER_CSV = r'C:\Users\conni\racecar_docker\home\racecar_ws\rss_lab3\lab03\bags\base_case\base_case_0.db\vesc\low_level\ackermann_cmd.csv'
# # df_steer = pd.read_csv(STEER_CSV).sort_values('time').reset_index(drop=True)

# # def compute_error(row, side, velocity, desired_distance):
# #     """Replicates the slice_scan logic from bag_grapher.py"""
    
# #     # Pull ranges from the row
# #     range_cols = [f'ranges_{i}' for i in range(1081)]
# #     ranges = row[range_cols].values.astype(float)

# #     range_min = row['range_min']
# #     range_max = row['range_max']
# #     angle_min = row['angle_min']
# #     angle_max = row['angle_max']

# #     # Reconstruct angles
# #     all_angles = np.linspace(angle_min, angle_max, len(ranges))

# #     # Valid range mask
# #     valid_mask = (ranges > range_min) & (ranges < range_max)

# #     # Side mask (left or right wall)
# #     if side == 1:
# #         wall_mask = valid_mask & (all_angles > (np.pi / 3.0)) & (all_angles < (115.0 * np.pi / 180.0))
# #     else:
# #         wall_mask = valid_mask & (all_angles < -(np.pi / 3.0)) & (all_angles > -(115.0 * np.pi / 180.0))

# #     wall_distances = ranges[wall_mask]
# #     needed_angles  = all_angles[wall_mask]

# #     # Convert to cartesian
# #     all_x = wall_distances * np.cos(needed_angles)
# #     all_y = wall_distances * np.sin(needed_angles)

# #     # Outlier removal via median
# #     if len(all_y) == 0:
# #         return 0.0

# #     median_y  = np.median(all_y)
# #     tolerance = 0.4
# #     good_mask = np.abs(all_y - median_y) < tolerance
# #     good_x    = all_x[good_mask]
# #     good_y    = all_y[good_mask]

# #     # Edge cases
# #     if len(good_x) < 2:
# #         return float(0.34 * side)

# #     if np.ptp(good_x) < 0.1:
# #         return 0.0

# #     # Linear regression → predicted wall distance
# #     m, c = np.polyfit(good_x, good_y, 1)
# #     x_offset    = velocity * 0.5
# #     y_at_offset = (m * x_offset) + c

# #     # Front wall emergency detection
# #     front_mask   = valid_mask & (all_angles > -0.2) & (all_angles < 0.2)
# #     front_ranges = ranges[front_mask]

# #     front_error = 0.0
# #     if len(front_ranges) > 0:
# #         front_dist = np.min(front_ranges)
# #         safe_dist  = desired_distance * velocity
# #         if front_dist < safe_dist:
# #             front_error = (safe_dist - front_dist) * 2.0

# #     error = desired_distance - abs(y_at_offset) + front_error
# #     # percent_error = abs(exp_error / desired_distance)  * 100.0

# #     return error


# # # ── LOAD DATA ────────────────────────────────────────────────────────────────
# # print("Loading CSV...")
# # # df = pd.read_csv(CSV_PATH, sep=',t')  # change sep=',' if comma-separated
# # df = pd.read_csv(CSV_PATH)  # default sep=','
# # df = df.sort_values('time').reset_index(drop=True)

# # # Then convert timestamps as before
# # timestamps = pd.to_datetime(df['time']).astype('int64') / 1e9
# # t0         = timestamps.iloc[0]
# # time_secs  = (timestamps - t0).values


# # # ── COMPUTE ERROR FOR EVERY ROW ───────────────────────────────────────────────
# # print("Computing error...")
# # errors = []
# # for _, row in df.iterrows():
# #     e = (abs(compute_error(row, SIDE, VELOCITY, DESIRED_DISTANCE))/DESIRED_DISTANCE) *100
# #     errors.append(e)

# # errors = np.array(errors)

# # # Set your desired start time (in seconds relative to t0)
# # START_TIME = 0  # e.g. skip the first 30 seconds

# # # Trim both arrays
# # mask              = time_secs >= START_TIME
# # time_secs_trimmed = time_secs[mask]
# # errors_trimmed    = errors[mask]

# # steer_timestamps = pd.to_datetime(df_steer['time']).astype('int64') / 1e9
# # steer_time_secs  = (steer_timestamps - t0).values  # use same t0 as scan

# # # Trim to same start time
# # steer_mask       = steer_time_secs >= START_TIME
# # steer_time_trimmed  = steer_time_secs[steer_mask]
# # steering_trimmed = df_steer['drive_steering_angle'][steer_mask].values  # adjust column name

# # fig, ax1 = plt.subplots(figsize=(14, 6))

# # # ── Plot 1: Error on left y-axis ──
# # color_error = 'steelblue'
# # ax1.set_xlabel('Time (s)')
# # ax1.set_ylabel('Error (% of desired distance)', color=color_error)
# # ax1.plot(time_secs_trimmed, errors_trimmed, color=color_error, linewidth=1.2, label='Error')
# # ax1.axhline(0, color=color_error, linestyle='--', linewidth=0.8, alpha=0.5)
# # ax1.tick_params(axis='y', labelcolor=color_error)
# # ax1.grid(True, alpha=0.3)

# # # ── Plot 2: Steering angle on right y-axis ──
# # ax2 = ax1.twinx()  # shares the same x-axis
# # color_steer = 'darkorange'
# # ax2.set_ylabel('Steering Angle (rad)', color=color_steer)
# # ax2.plot(steer_time_trimmed, steering_trimmed, color=color_steer, linewidth=1.2, label='Steering Angle')
# # ax2.tick_params(axis='y', labelcolor=color_steer)

# # # ── Align both y-axes so 0 is at the same position ──
# # ax1_ylim = ax1.get_ylim()
# # ax2_ylim = ax2.get_ylim()

# # # Find the largest range needed on each side of 0
# # ax1_max = max(abs(ax1_ylim[0]), abs(ax1_ylim[1]))
# # ax2_max = max(abs(ax2_ylim[0]), abs(ax2_ylim[1]))

# # # Set both axes to be symmetric around 0
# # ax1.set_ylim(-ax1_max, ax1_max)
# # ax2.set_ylim(-ax2_max, ax2_max)

# # # ── Combined legend ──
# # lines1, labels1 = ax1.get_legend_handles_labels()
# # lines2, labels2 = ax2.get_legend_handles_labels()
# # ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

# # plt.title('Error % vs Steering Angle over Time')
# # plt.tight_layout()
# # plt.savefig('error_vs_steering.png', dpi=150)
# # plt.show()


# # # # ── PLOT ──────────────────────────────────────────────────────────────────────
# # # fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# # # # Error over time
# # # axes[0].plot(time_secs_trimmed, errors_trimmed, color='steelblue', linewidth=1.2)
# # # axes[0].axhline(0, color='red', linestyle='--', linewidth=1, label='Zero error')
# # # axes[0].set_ylabel('Error (m)')
# # # axes[0].set_title('Wall Following Error for Base Case over Time')
# # # axes[0].legend()
# # # axes[0].grid(True, alpha=0.3)

# # # # Absolute error
# # # axes[1].plot(time_secs_trimmed, np.abs(errors_trimmed), color='darkorange', linewidth=1.2)
# # # axes[1].set_ylabel('|Error| (m)')
# # # axes[1].set_xlabel('Time (s)')
# # # axes[1].set_title('Absolute Error for Base Case over Time')
# # # axes[1].grid(True, alpha=0.3)

# # # plt.tight_layout()
# # # plt.savefig('base_case0_error_plot.png', dpi=150)
# # # plt.show()

# # print(f"\nStats:")
# # print(f"  Mean error:     {np.mean(errors):.4f} m")
# # print(f"  Mean |error|:   {np.mean(np.abs(errors)):.4f} m")
# # print(f"  Max |error|:    {np.max(np.abs(errors)):.4f} m")
# # print(f"  Std dev:        {np.std(errors):.4f} m")