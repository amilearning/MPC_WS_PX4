## *********************************************************
##
## File autogenerated for the mav_disturbance_observer package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'remove constant offsets', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'calibrate', 'edit_method': '', 'default': False, 'level': 0, 'min': False, 'type': 'bool'}, {'srcline': 291, 'description': 'position noise', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_position', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'velocity noise', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_velocity', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'attitude noise', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_attitude', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'angular velocity noise', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_angular_velocity', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'external force noise', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_force', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'external torque noise', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'q_torque', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'position meas noise', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r_position', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'velocity meas noise', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r_velocity', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.001, 'type': 'double'}, {'srcline': 291, 'description': 'attitude meas noise', 'max': 10.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'r_attitude', 'edit_method': '', 'default': 0.1, 'level': 0, 'min': 0.001, 'type': 'double'}], 'type': '', 'id': 0}

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

