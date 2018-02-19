import numpy as np
from data import Data
from transformation import Transformation
from pyquaternion import Quaternion

if __name__ == "__main__":
    # Objects
    data_obj = Data()
    T_obj = Transformation()
    data_keys = data_obj.return_data_keys() 

    for data_key in data_keys:
        print '\n[ STATUS ] data_key: {}'.format(data_key)

        position = data_obj.return_vicon_position(data_key)
        quat = data_obj.return_vicon_quat(data_key)
        T_vicon_to_wand = T_obj.convert_to_T_matrix(position, quat)
        T_vicon_to_wand_position, T_vicon_to_wand_quat = \
            T_obj.convert_T_matrix_to_position_and_quat(T_vicon_to_wand)
        print 'T_vicon_to_wand: \nPos (x y z): {}\nQuat (w x y z): {}'.format(
           T_vicon_to_wand_position, T_vicon_to_wand_quat)

        position = data_obj.return_opti_position(data_key)
        quat = data_obj.return_opti_quat(data_key)
        T_opti_to_wand = T_obj.convert_to_T_matrix(position, quat)
        T_opti_to_wand_position, T_opti_to_wand_quat = \
            T_obj.convert_T_matrix_to_position_and_quat(T_opti_to_wand)
        print 'T_opti_to_wand: \nPos (x y z): {}\nQuat (w x y z): {}'.format(
            T_opti_to_wand_position, T_opti_to_wand_quat)

        T_wand_to_opti = T_obj.inverse_matrix(T_opti_to_wand)
        T_wand_to_opti_position, T_wand_to_opti_quat = \
            T_obj.convert_T_matrix_to_position_and_quat(T_wand_to_opti)
        print 'T_wand_to_opti: \nPos (x y z): {}\nQuat (w x y z): {}'.format(
            T_wand_to_opti_position, T_wand_to_opti_quat)

        T_vicon_to_opti = np.dot(T_vicon_to_wand, T_wand_to_opti)
        T_vicon_to_opti_position, T_vicon_to_opti_quat = \
            T_obj.convert_T_matrix_to_position_and_quat(T_vicon_to_opti)
        print 'T_vicon_to_opti: \nPos (x y z): {}\nQuat (w x y z): {}'.format(
            T_vicon_to_opti_position, T_vicon_to_opti_quat)

