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
