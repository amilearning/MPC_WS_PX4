# -*- coding: utf-8 -*-
from __future__ import print_function

import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/melodic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/melodic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in '/home/slam01/dronw_ws/MPC_WS_PX4/devel;/home/slam01/catkin_ws_PBVS_yawfused/devel;/home/slam01/catkin_ws_viconbridge/devel;/home/slam01/catkin_ws_ublox/devel;/home/slam01/catkin_ws_mocap_optitrack/devel;/home/slam01/catkin_ws_bag2csv/devel;/home/slam01/catkin_ws_aruco_5x5/devel;/home/slam01/catkin_ws_aruco_7x7/devel;/home/slam01/catkin_ws_matlab/devel;/home/slam01/catkin_ws_optitrack_test/devel;/home/slam01/catkin_ws_vrpn/devel;/home/slam01/catkin_ws/devel;/opt/ros/melodic'.split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/slam01/dronw_ws/MPC_WS_PX4/devel/.private/mav_state_machine_msgs/env.sh')

output_filename = '/home/slam01/dronw_ws/MPC_WS_PX4/build/mav_state_machine_msgs/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    # print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
