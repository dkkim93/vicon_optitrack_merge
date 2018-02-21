import rosbag
import numpy as np
import matplotlib.pyplot as plt
from data import Data
from transformation import Transformation
from draw import Draw
from acl_msgs.msg import ViconState
from geometry_msgs.msg import PoseStamped
from decimal import Decimal

def return_timestamp(data):
    nsec = str(data.header.stamp.nsecs)
    if len(nsec) == 7:
        nsec = str(00) + nsec # Append 0 for digits that missed 0 in front
    if len(nsec) == 8:
        nsec = str(0) + nsec # Append 0 for digits that missed 0 in front

    ts = str(data.header.stamp.secs) + "." + nsec
    if len(ts) != 20:
        RuntimeError("Timestamp does not match!")

    return Decimal(ts)

def vicon_cb(data, data_obj):
    ts = return_timestamp(data)

    # Put timestamp, position, and quat into list and append
    vicon_list = [ts, data.pose.position.x, data.pose.position.y, data.pose.position.z,
                  data.pose.orientation.w, data.pose.orientation.x, data.pose.orientation.y,
                  data.pose.orientation.z]
    data_obj.add_vicon_data(vicon_list)

def opti_cb(data, T_vicon_to_opti, data_obj):
    ts = return_timestamp(data)

    # position and quat
    position = np.array([data.pose.position.x, 
                         data.pose.position.y, 
                         data.pose.position.z])
    quat     = np.array([data.pose.orientation.w,
                         data.pose.orientation.x,
                         data.pose.orientation.y,
                         data.pose.orientation.z])

    opti_orig_list = [ts, data.pose.position.x, data.pose.position.y, data.pose.position.z,
                      data.pose.orientation.w, data.pose.orientation.x, data.pose.orientation.y,
                      data.pose.orientation.z]
    data_obj.add_opti_orig_data(opti_orig_list)

    # Transformation
    T_opti_to_wand = T_obj.convert_to_T_matrix(position, quat)
    T_vicon_to_wand = np.dot(T_vicon_to_opti, T_opti_to_wand)

    opti_position, opti_quat = \
        T_obj.convert_T_matrix_to_position_and_quat(T_vicon_to_wand)

    opti_list = [ts, opti_position[0], opti_position[1], opti_position[2],
                 opti_quat[0], opti_quat[1], opti_quat[2], opti_quat[3]]
    data_obj.add_opti_data(opti_list)

if __name__ == "__main__":
    # Class initialization
    data_obj = Data()
    T_obj    = Transformation()
    draw_obj = Draw()

    T_vicon_to_opti = T_obj.return_T_vicon_to_opti()

    # Read data and store 
    # bag = rosbag.Bag("../../data/data_trajectory/optitrack/2018-02-19-18-02-18.bag")
    bag = rosbag.Bag("../../data/data_trajectory/optitrack/2018-02-19-18-10-05.bag")
    vicon_topic = "/dongki/vicon"
    opti_topic  = "/Robot_2/pose"
    for topic, msg, t in bag.read_messages(topics=[opti_topic, vicon_topic]):
        if topic == "/dongki/vicon":
            vicon_cb(msg, data_obj)
        elif topic == "/Robot_2/pose":
            opti_cb(msg, T_vicon_to_opti, data_obj)
        else:
            RuntimeError("Non-valid topic found.")
    data_obj.set_vicon()
    data_obj.set_opti()
    data_obj.set_opti_orig()
    import sys; sys.exit()

    # Further optimize T
    data_obj.optimize_T()

    # Draw plot
    draw_obj.draw_plot(data_obj.vicon_ts, data_obj.vicon_x,
                       data_obj.opti_ts, data_obj.opti_x,
                       'Position x', 'Timestamp (UNIX)', 'Meter',
                       'Vicon', 'OptiTrack')

    draw_obj.draw_plot(data_obj.vicon_ts, data_obj.vicon_y,
                       data_obj.opti_ts, data_obj.opti_y,
                       'Position y', 'Timestamp (UNIX)', 'Meter',
                       'Vicon', 'OptiTrack')

    draw_obj.draw_plot(data_obj.vicon_ts, data_obj.vicon_z,
                       data_obj.opti_ts, data_obj.opti_z,
                       'Position z', 'Timestamp (UNIX)', 'Meter',
                       'Vicon', 'OptiTrack')

    draw_obj.draw_plot(data_obj.vicon_ts, data_obj.vicon_qw,
                       data_obj.opti_ts, data_obj.opti_qw,
                       'Quaternion w', 'Timestamp (UNIX)', 'Meter',
                       'Vicon', 'OptiTrack')

    draw_obj.draw_plot(data_obj.vicon_ts, data_obj.vicon_qx,
                       data_obj.opti_ts, data_obj.opti_qx,
                       'Quaternion x', 'Timestamp (UNIX)', 'Meter',
                       'Vicon', 'OptiTrack')

    draw_obj.draw_plot(data_obj.vicon_ts, data_obj.vicon_qy,
                       data_obj.opti_ts, data_obj.opti_qy,
                       'Quaternion y', 'Timestamp (UNIX)', 'Meter',
                       'Vicon', 'OptiTrack')

    draw_obj.draw_plot(data_obj.vicon_ts, data_obj.vicon_qz,
                       data_obj.opti_ts, data_obj.opti_qz,
                       'Quaternion z', 'Timestamp (UNIX)', 'Meter',
                       'Vicon', 'OptiTrack')
    plt.show()
