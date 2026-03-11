import glob
import os
from setuptools import find_packages
from setuptools import setup

package_name = 'lab03'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/'+package_name, ['package.xml', "lab03/params.yaml"]),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/lab03/launch', glob.glob(os.path.join('launch', '*launch.xml'))),
        ('share/lab03/launch', glob.glob(os.path.join('launch', '*launch.py')))],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Sebastian',
    maintainer_email='sebastianag2002@gmail.com',
    description='Wall Follower ROS2 Package',
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'wall_follower = lab03.wall_follower_2:main',
	        'viz_example = lab03.viz_example:main',
        	'test_wall_follower = lab03.test_wall_follower:main',
            'safety_stop = lab03.safety_feature:main',
            'bag_grapher = lab03.bag_grapher:main',
            'drive_forward = lab03.safety_test.py'
        ],
    },
)
