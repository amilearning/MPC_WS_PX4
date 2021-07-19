## *********************************************************
##
## File autogenerated for the mav_linear_mpc package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'Penality on x axis pos', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_x', 'edit_method': '', 'default': 50.0, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on y axis pos', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_y', 'edit_method': '', 'default': 50.0, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on z axis pos', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_z', 'edit_method': '', 'default': 80.0, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on x axis vel', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_vx', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on y axis vel', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_vy', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on z axis vel', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_vz', 'edit_method': '', 'default': 35.0, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on roll state', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_roll', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on pitch state', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_pitch', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on roll cmd', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r_roll', 'edit_method': '', 'default': 30.0, 'level': 0, 'min': 1e-05, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on pitch cmd', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r_pitch', 'edit_method': '', 'default': 30.0, 'level': 0, 'min': 0.0001, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on thrust cmd', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r_thrust', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': 1e-05, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on delta roll cmd', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r_droll', 'edit_method': '', 'default': 0.26, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on delta pitch cmd', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r_dpitch', 'edit_method': '', 'default': 0.26, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 291, 'description': 'Penality on delta thrust cmd', 'max': 0.1, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r_dthrust', 'edit_method': '', 'default': 0.01, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'max roll cmd [rad]', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'roll_max', 'edit_method': '', 'default': 0.45, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 291, 'description': 'max pitch cmd [rad]', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'pitch_max', 'edit_method': '', 'default': 0.45, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 291, 'description': 'max yawrate cmd [rad/s]', 'max': 2.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'yaw_rate_max', 'edit_method': '', 'default': 1.5, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 291, 'description': 'min thrust cmd [m/s2]', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'thrust_min', 'edit_method': '', 'default': 5.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'max thrust cmd [m/s2]', 'max': 50.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'thrust_max', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'yaw gain', 'max': 2.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'K_yaw', 'edit_method': '', 'default': 0.5, 'level': 0, 'min': 0.01, 'type': 'double'}, {'srcline': 291, 'description': 'integrator gain for xy', 'max': 3.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'Ki_xy', 'edit_method': '', 'default': 0.2, 'level': 0, 'min': 0.01, 'type': 'double'}, {'srcline': 291, 'description': 'integrator gain for altitude', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'Ki_altitude', 'edit_method': '', 'default': 0.2, 'level': 0, 'min': 0.01, 'type': 'double'}, {'srcline': 291, 'description': 'XY offset free MPC', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'enable_offset_free', 'edit_method': '', 'default': True, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'integral action', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'enable_integrator', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

