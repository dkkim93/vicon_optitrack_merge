import numpy as np

class Data(object):
    def __init__(self):
        self.vicon_positions = {} 
        self.opti_positions  = {} 
        self.vicon_quats     = {} 
        self.opti_quats      = {} 

        self._add_vicon_data()
        self._add_opti_data()
        self._check_err()

    def _add_vicon_data(self):
        # Data 1
        position = np.array([1.27146427388, 0.0982186137085, 0.0617510854658]) # x y z
        self._add_to_dict(self.vicon_positions, 'data_1', position)

        quat = np.array([0.999339563026, 0.00527315805089, 0.00285273824411, 0.0358398306381]) # w x y z
        self._add_to_dict(self.vicon_quats, 'data_1', quat)

        # Data 2
        position = np.array([1.57233373329, -0.831640912928, 0.075050328159]) # x y z
        self._add_to_dict(self.vicon_positions, 'data_2', position)

        quat = np.array([0.999677851675, 0.00428298586649, 0.00157737908313, 0.0249671940125])  # w x y z
        self._add_to_dict(self.vicon_quats, 'data_2', quat)

        # Data 3
        position = np.array([1.54398658889, -0.410228881554, 1.16198586478]) # x y z
        self._add_to_dict(self.vicon_positions, 'data_3', position)

        quat = np.array([0.999571524024, -0.000650802997162, 0.00282766945741, -0.0291264330444]) # w x y z
        self._add_to_dict(self.vicon_quats, 'data_3', quat)

        # Data 4
        position = np.array([0.661849322701, -1.56916648039, 1.17596197592]) # x y z
        self._add_to_dict(self.vicon_positions, 'data_4', position)

        quat = np.array([0.987117015305, 0.00537348658354, 0.00700438753698, 0.159756259006]) # w x y z
        self._add_to_dict(self.vicon_quats, 'data_4', quat)

    def _add_opti_data(self):
        # Data 1
        position = np.array([-0.0284148845822, 10.7996358871, 0.0901763662696]) # x y z
        self._add_to_dict(self.opti_positions, 'data_1', position)

        quat = np.array([-0.700189054012, -0.00834508985281, 0.00316851167008, 0.713901758194]) # w x y z
        self._add_to_dict(self.opti_quats, 'data_1', quat)

        # Data 2
        position = np.array([-0.973524987698, 10.5920934677, 0.0921021774411]) # x y z
        self._add_to_dict(self.opti_positions, 'data_2', position)

        quat = np.array([0.691749215126, 0.00779610266909, 0.00198522815481, -0.722093045712]) # w x y z
        self._add_to_dict(self.opti_quats, 'data_2', quat)

        # Data 3
        position = np.array([-0.56702709198, 10.5713949203, 1.17146623135]) # x y z
        self._add_to_dict(self.opti_positions, 'data_3', position)

        quat = np.array([0.652602374554, 0.0024211734999, 0.00287404307164, -0.757691323757]) # w x y z
        self._add_to_dict(self.opti_quats, 'data_3', quat)

        # Data 4
        position = np.array([-1.6251026392, 11.5489768982, 1.18096828461]) # x y z
        self._add_to_dict(self.opti_positions, 'data_4', position)

        quat = np.array([-0.782936692238, -0.00750978616998, 0.000981374876574, 0.622055411339])
        self._add_to_dict(self.opti_quats, 'data_4', quat)

    def _add_to_dict(self, target_dict, key, data):
        target_dict[key] = data

    def _check_err(self):
        if len(self.vicon_positions.keys()) != len(self.vicon_quats.keys()):
            RuntimeError("[ ERROR ] vicon positions and quats don't have same number of data")

        if len(self.opti_positions.keys()) != len(self.opti_quats.keys()):
            RuntimeError("[ ERROR ] opti positions and quats don't have same number of data")

        if len(self.vicon_positions.keys()) != len(self.opti_positions.keys()):
            RuntimeError("[ ERROR ] vicon and opti don't have same number of data")

    def return_data_keys(self):
        return self.vicon_positions.keys()

    def return_vicon_position(self, key):
        return self.vicon_positions[key]

    def return_vicon_quat(self, key):
        return self.vicon_quats[key]

    def return_opti_position(self, key):
        return self.opti_positions[key]

    def return_opti_quat(self, key):
        return self.opti_quats[key]
