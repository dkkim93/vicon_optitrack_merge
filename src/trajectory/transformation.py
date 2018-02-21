import numpy as np
from pyquaternion import Quaternion

class Transformation(object):
    def __init__(self):
        self.T_vicon_to_opti_position = np.array([12.0174229, 
                                                  1.11216997, 
                                                  -0.0175561])
        self.T_vicon_to_opti_quat = np.array([0.67402662, 
                                              -0.00083867, 
                                              0.00084894, 
                                              0.7387037]) # w x y z
        self.T_vicon_to_opti = self.convert_to_T_matrix(self.T_vicon_to_opti_position, 
                                                        self.T_vicon_to_opti_quat)

    def return_T_vicon_to_opti(self):
        return self.T_vicon_to_opti

    def convert_to_T_matrix(self, position, quat):
        R_matrix = self._convert_quat_to_R_matrix(quat)
        T_matrix = np.zeros((4, 4))

        T_matrix[0, 0] = R_matrix[0, 0]
        T_matrix[0, 1] = R_matrix[0, 1]
        T_matrix[0, 2] = R_matrix[0, 2]
        T_matrix[0, 3] = position[0]

        T_matrix[1, 0] = R_matrix[1, 0]
        T_matrix[1, 1] = R_matrix[1, 1]
        T_matrix[1, 2] = R_matrix[1, 2]
        T_matrix[1, 3] = position[1]

        T_matrix[2, 0] = R_matrix[2, 0]
        T_matrix[2, 1] = R_matrix[2, 1]
        T_matrix[2, 2] = R_matrix[2, 2]
        T_matrix[2, 3] = position[2]

        T_matrix[3, 0] = 0
        T_matrix[3, 1] = 0
        T_matrix[3, 2] = 0
        T_matrix[3, 3] = 1

        return T_matrix

    def inverse_matrix(self, T_matrix):
        R_matrix = T_matrix[0:3, 0:3]
        R_inv_matrix = R_matrix.transpose()

        position = T_matrix[0:3, 3].reshape((3, 1))
        position_inv = np.dot(-R_inv_matrix, position)

        T_matrix = np.zeros((4, 4))

        T_matrix[0, 0] = R_inv_matrix[0, 0]
        T_matrix[0, 1] = R_inv_matrix[0, 1]
        T_matrix[0, 2] = R_inv_matrix[0, 2]
        T_matrix[0, 3] = position_inv[0]

        T_matrix[1, 0] = R_inv_matrix[1, 0]
        T_matrix[1, 1] = R_inv_matrix[1, 1]
        T_matrix[1, 2] = R_inv_matrix[1, 2]
        T_matrix[1, 3] = position_inv[1]

        T_matrix[2, 0] = R_inv_matrix[2, 0]
        T_matrix[2, 1] = R_inv_matrix[2, 1]
        T_matrix[2, 2] = R_inv_matrix[2, 2]
        T_matrix[2, 3] = position_inv[2]

        T_matrix[3, 0] = 0
        T_matrix[3, 1] = 0
        T_matrix[3, 2] = 0
        T_matrix[3, 3] = 1

        return T_matrix

    def convert_T_matrix_to_position_and_quat(self, T_matrix):
        position = T_matrix[0:3, 3]
        R_matrix = T_matrix[0:3, 0:3]

        return position, self._convert_R_matrix_to_quat(R_matrix)

    def _convert_R_matrix_to_quat(self, R_matrix):
        quat_obj = Quaternion(matrix=R_matrix)
        quat_obj = quat_obj.normalised
        return np.array([quat_obj[0], quat_obj[1], quat_obj[2], quat_obj[3]]) # w x y z

    def _convert_quat_to_R_matrix(self, quat):
        quat_obj = Quaternion(quat)
        quat_obj = quat_obj.normalised
        return quat_obj.rotation_matrix
