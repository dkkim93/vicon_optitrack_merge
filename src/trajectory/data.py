import numpy as np

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

    def add_vicon_data(self, data):
        self.vicon_lists.append(data)

    def add_opti_data(self, data):
        self.opti_lists.append(data)

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

            if (x_diff <= 0.03) and (y_diff <= 0.03) and (z_diff <= 0.03):
                print '\nqw:', self.vicon_qw[vicon_idx], 'vs', self.opti_qw[opti_idx]
                print 'qx:', self.vicon_qx[vicon_idx], 'vs', self.opti_qx[opti_idx]
                print 'qy:', self.vicon_qy[vicon_idx], 'vs', self.opti_qy[opti_idx]
                print 'qz:', self.vicon_qz[vicon_idx], 'vs', self.opti_qz[opti_idx]
