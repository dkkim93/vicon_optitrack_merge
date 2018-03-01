import numpy as np
from transformation import Transformation

class Data(object):
    def __init__(self):
        self.vicon_lists = []
        self.vicon_ts    = []
        self.vicon_x     = []
        self.vicon_y     = []
        self.vicon_z     = []
        self.vicon_qw    = []
        self.vicon_qx    = []
        self.vicon_qy    = []
        self.vicon_qz    = []

        self.opti_lists  = []
        self.opti_ts     = []
        self.opti_x      = []
        self.opti_y      = []
        self.opti_z      = []
        self.opti_qw     = []
        self.opti_qx     = []
        self.opti_qy     = []
        self.opti_qz     = []

        self.opti_orig_lists = [] # Original (i.e., opti to wand) before transformation
        self.opti_orig_ts    = []
        self.opti_orig_x     = []
        self.opti_orig_y     = []
        self.opti_orig_z     = []
        self.opti_orig_qw    = []
        self.opti_orig_qx    = []
        self.opti_orig_qy    = []
        self.opti_orig_qz    = []

        self.T_ts = []
        self.T_x = []
        self.T_y = []
        self.T_z = []
        self.T_qw = []
        self.T_qx = []
        self.T_qy = []
        self.T_qz = []

        self.T_vicon_to_opti_positions = []
        self.T_vicon_to_opti_quats     = []

        self.T_obj = Transformation()

    def add_vicon_data(self, data):
        self.vicon_lists.append(data)

    def add_opti_data(self, data):
        self.opti_lists.append(data)

    def add_opti_orig_data(self, data):
        self.opti_orig_lists.append(data)

    def set_vicon(self):
        self.vicon_ts = np.asarray([data[0] for data in self.vicon_lists])
        self.vicon_x  = np.asarray([data[1] for data in self.vicon_lists])
        self.vicon_y  = np.asarray([data[2] for data in self.vicon_lists])
        self.vicon_z  = np.asarray([data[3] for data in self.vicon_lists])
        self.vicon_qw = np.asarray([data[4] for data in self.vicon_lists])
        self.vicon_qx = np.asarray([data[5] for data in self.vicon_lists])
        self.vicon_qy = np.asarray([data[6] for data in self.vicon_lists])
        self.vicon_qz = np.asarray([data[7] for data in self.vicon_lists])

    def set_opti(self):
        self.opti_ts = np.asarray([data[0] for data in self.opti_lists])
        self.opti_x  = np.asarray([data[1] for data in self.opti_lists])
        self.opti_y  = np.asarray([data[2] for data in self.opti_lists])
        self.opti_z  = np.asarray([data[3] for data in self.opti_lists])
        self.opti_qw = np.asarray([data[4] for data in self.opti_lists])
        self.opti_qx = np.asarray([data[5] for data in self.opti_lists])
        self.opti_qy = np.asarray([data[6] for data in self.opti_lists])
        self.opti_qz = np.asarray([data[7] for data in self.opti_lists])

    def set_opti_orig(self):
        self.opti_orig_ts = np.asarray([data[0] for data in self.opti_orig_lists])
        self.opti_orig_x  = np.asarray([data[1] for data in self.opti_orig_lists])
        self.opti_orig_y  = np.asarray([data[2] for data in self.opti_orig_lists])
        self.opti_orig_z  = np.asarray([data[3] for data in self.opti_orig_lists])
        self.opti_orig_qw = np.asarray([data[4] for data in self.opti_orig_lists])
        self.opti_orig_qx = np.asarray([data[5] for data in self.opti_orig_lists])
        self.opti_orig_qy = np.asarray([data[6] for data in self.opti_orig_lists])
        self.opti_orig_qz = np.asarray([data[7] for data in self.opti_orig_lists])

    def find_nearest_idx(self, array, value):
        idx = (np.abs(array-value)).argmin()
        return idx

    def diff(self, value_1, value_2):
        return np.absolute(value_1 - value_2)

    def optimize_T(self):
        for vicon_idx in range(len(self.vicon_ts)):
            opti_idx = self.find_nearest_idx(self.opti_ts, self.vicon_ts[vicon_idx])

            x_diff = self.diff(self.vicon_x[vicon_idx], self.opti_x[opti_idx])
            y_diff = self.diff(self.vicon_y[vicon_idx], self.opti_y[opti_idx])
            z_diff = self.diff(self.vicon_z[vicon_idx], self.opti_z[opti_idx])
            qw_diff = self.diff(np.absolute(self.vicon_qw[vicon_idx]), np.absolute(self.opti_qw[opti_idx]))
            qx_diff = self.diff(np.absolute(self.vicon_qx[vicon_idx]), np.absolute(self.opti_qx[opti_idx]))
            qy_diff = self.diff(np.absolute(self.vicon_qy[vicon_idx]), np.absolute(self.opti_qy[opti_idx]))
            qz_diff = self.diff(np.absolute(self.vicon_qz[vicon_idx]), np.absolute(self.opti_qz[opti_idx]))

            if x_diff <= 0.03 and y_diff <= 0.03 and z_diff <= 0.03 and \
               qw_diff <= 0.03 and qx_diff <= 0.03 and qy_diff <= 0.03 and qz_diff <= 0.03:
                # T_vicon_to_wand
                T_vicon_to_wand = self.T_obj.convert_to_T_matrix(
                    position=np.array([self.vicon_x[vicon_idx],
                                       self.vicon_y[vicon_idx],
                                       self.vicon_z[vicon_idx]]),
                    quat=np.array([self.vicon_qw[vicon_idx],
                                   self.vicon_qx[vicon_idx],
                                   self.vicon_qy[vicon_idx],
                                   self.vicon_qz[vicon_idx]]))

                # T_opti_to_wand
                T_opti_to_wand = self.T_obj.convert_to_T_matrix(
                    position=np.array([self.opti_orig_x[opti_idx],
                                       self.opti_orig_y[opti_idx],
                                       self.opti_orig_z[opti_idx]]),
                    quat=np.array([self.opti_orig_qw[opti_idx],
                                   self.opti_orig_qx[opti_idx],
                                   self.opti_orig_qy[opti_idx],
                                   self.opti_orig_qz[opti_idx]]))

                # T_wand_to_opti
                T_wand_to_opti = self.T_obj.inverse_matrix(T_opti_to_wand)

                # T_vicon_to_opti
                T_vicon_to_opti = np.dot(T_vicon_to_wand, T_wand_to_opti)
                
                T_vicon_to_opti_position, T_vicon_to_opti_quat = \
                    self.T_obj.convert_T_matrix_to_position_and_quat(T_vicon_to_opti)
                print 'T_vicon_to_opti: \nPos (x y z): {}\nQuat (w x y z): {}'.format(
                    T_vicon_to_opti_position, T_vicon_to_opti_quat)  
                
                # Save result
                self.T_vicon_to_opti_positions.append(T_vicon_to_opti_position)
                self.T_vicon_to_opti_quats.append(T_vicon_to_opti_quat)

                # Add data for visualization
                self.T_ts.append(self.opti_ts[opti_idx])
                self.T_x.append(self.opti_x[opti_idx])
                self.T_y.append(self.opti_y[opti_idx])
                self.T_z.append(self.opti_z[opti_idx])
                self.T_qw.append(self.opti_qw[opti_idx])
                self.T_qx.append(self.opti_qx[opti_idx])
                self.T_qy.append(self.opti_qy[opti_idx])
                self.T_qz.append(self.opti_qz[opti_idx])

        print len(self.T_vicon_to_opti_positions)
        print np.mean(self.T_vicon_to_opti_positions, axis=0)
        print np.mean(self.T_vicon_to_opti_quats, axis=0)

    def error(self):
        x_err  = []
        y_err  = []
        z_err  = []
        qx_err = []
        qy_err = []
        qz_err = []
        qw_err = []

        self.vicon_ts = self.vicon_ts[::5]
        self.vicon_x  = self.vicon_x[::5]
        self.vicon_y  = self.vicon_y[::5]
        self.vicon_z  = self.vicon_z[::5]
        self.vicon_qw = self.vicon_qw[::5]
        self.vicon_qx = self.vicon_qx[::5]
        self.vicon_qy = self.vicon_qy[::5]
        self.vicon_qz = self.vicon_qz[::5]

        self.opti_ts = self.opti_ts[::5]
        self.opti_x  = self.opti_x[::5]
        self.opti_y  = self.opti_y[::5]
        self.opti_z  = self.opti_z[::5]
        self.opti_qw = self.opti_qw[::5]
        self.opti_qx = self.opti_qx[::5]
        self.opti_qy = self.opti_qy[::5]
        self.opti_qz = self.opti_qz[::5]

        for vicon_idx in range(len(self.vicon_ts)):
            print vicon_idx, '/', len(self.vicon_ts)
            opti_idx = self.find_nearest_idx(self.opti_ts, self.vicon_ts[vicon_idx])

            if self.diff(self.vicon_ts[vicon_idx], self.opti_ts[opti_idx]) < 0.1:
                x_err.append(self.diff(self.vicon_x[vicon_idx], self.opti_x[opti_idx]))
                y_err.append(self.diff(self.vicon_y[vicon_idx], self.opti_y[opti_idx]))
                z_err.append(self.diff(self.vicon_z[vicon_idx], self.opti_z[opti_idx]))
                qw_err.append(self.diff(self.vicon_qw[vicon_idx], -self.opti_qw[opti_idx]))
                qx_err.append(self.diff(self.vicon_qx[vicon_idx], -self.opti_qx[opti_idx]))
                qy_err.append(self.diff(self.vicon_qy[vicon_idx], -self.opti_qy[opti_idx]))
                qz_err.append(self.diff(self.vicon_qz[vicon_idx], -self.opti_qz[opti_idx]))

        print np.mean(x_err)
        print np.mean(y_err)
        print np.mean(z_err)
        print np.mean(qw_err)
        print np.mean(qx_err)
        print np.mean(qy_err)
        print np.mean(qz_err)
