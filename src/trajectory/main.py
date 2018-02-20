import rosbag
import numpy as np
import matplotlib.pyplot as plt
from transformation import Transformation
from acl_msgs.msg import ViconState
from geometry_msgs.msg import PoseStamped
from decimal import Decimal

T_obj = Transformation()
T_vicon_to_opti = T_obj.convert_to_T_matrix(
    position=np.array([12.0174229, 1.11216997, -0.0175561]),
    quat=np.array([0.67402662, -0.00083867, 0.00084894, 0.7387037]))

vicon_timestamps, opti_timestamps = [], []

vicon_position_x, opti_position_x = [], []
vicon_position_y, opti_position_y = [], []
vicon_position_z, opti_position_z = [], []

vicon_quat_w, opti_quat_w = [], []
vicon_quat_x, opti_quat_x = [], []
vicon_quat_y, opti_quat_y = [], []
vicon_quat_z, opti_quat_z = [], []

def vicon_cb(data):
    timestamp = str(data.header.stamp.secs) + "." + str(data.header.stamp.nsecs)
    timestamp = Decimal(timestamp)

    vicon_timestamps.append(timestamp)

    vicon_position_x.append(data.pose.position.x)
    vicon_position_y.append(data.pose.position.y)
    vicon_position_z.append(data.pose.position.z)

    vicon_quat_w.append(data.pose.orientation.w)
    vicon_quat_x.append(data.pose.orientation.x)
    vicon_quat_y.append(data.pose.orientation.y)
    vicon_quat_z.append(data.pose.orientation.z)

def opti_cb(data):
    # Timestamp
    timestamp = str(data.header.stamp.secs) + "." + str(data.header.stamp.nsecs)
    timestamp = Decimal(timestamp)

    # position and quat
    position = np.array([data.pose.position.x, 
                         data.pose.position.y, 
                         data.pose.position.z])
    quat = np.array([data.pose.orientation.w,
                     data.pose.orientation.x,
                     data.pose.orientation.y,
                     data.pose.orientation.z])

    T_opti_to_wand = T_obj.convert_to_T_matrix(position, quat)
    T_vicon_to_wand = np.dot(T_vicon_to_opti, T_opti_to_wand)

    opti_position, opti_quat = \
        T_obj.convert_T_matrix_to_position_and_quat(T_vicon_to_wand)

    opti_timestamps.append(timestamp)

    opti_position_x.append(opti_position[0])
    opti_position_y.append(opti_position[1])
    opti_position_z.append(opti_position[2])

    opti_quat_w.append(opti_quat[0])
    opti_quat_x.append(opti_quat[1])
    opti_quat_y.append(opti_quat[2])
    opti_quat_z.append(opti_quat[3])

if __name__ == "__main__":
    bag = rosbag.Bag("../../data/data_trajectory/optitrack/2018-02-19-18-02-18.bag")

    for topic, msg, t in bag.read_messages(topics=["/Robot_2/pose", "/dongki/vicon"]):
        if topic == "/dongki/vicon":
            vicon_cb(msg)
        elif topic == "/Robot_2/pose":
            opti_cb(msg)
        else:
            RuntimeError("Non valid topic")

    plt.figure()
    plt.title('position_x')
    plt.xlabel('Timestamp')
    plt.ylabel('In meter')
    plt.plot(opti_timestamps, opti_position_x, label='opti')
    plt.plot(vicon_timestamps, vicon_position_x, label='vicon')
    plt.legend()

    plt.figure()
    plt.title('position_y')
    plt.xlabel('Timestamp')
    plt.ylabel('In meter')
    plt.plot(opti_timestamps, opti_position_y, label='opti')
    plt.plot(vicon_timestamps, vicon_position_y, label='vicon')
    plt.legend()

    plt.figure()
    plt.title('position_z')
    plt.xlabel('Timestamp')
    plt.ylabel('In meter')
    plt.plot(opti_timestamps, opti_position_z, label='opti')
    plt.plot(vicon_timestamps, vicon_position_z, label='vicon')
    plt.legend()

    plt.figure()
    plt.title('quat_x')
    plt.xlabel('Timestamp')
    plt.ylabel('Quaternion')
    plt.plot(opti_timestamps, opti_quat_x, label='opti')
    plt.plot(vicon_timestamps, vicon_quat_x, label='vicon')
    plt.legend()

    plt.figure()
    plt.title('quat_y')
    plt.xlabel('Timestamp')
    plt.ylabel('Quaternion')
    plt.plot(opti_timestamps, opti_quat_y, label='opti')
    plt.plot(vicon_timestamps, vicon_quat_y, label='vicon')
    plt.legend()

    plt.figure()
    plt.title('quat_z')
    plt.xlabel('Timestamp')
    plt.ylabel('Quaternion')
    plt.plot(opti_timestamps, opti_quat_z, label='opti')
    plt.plot(vicon_timestamps, vicon_quat_z, label='vicon')
    plt.legend()

    plt.figure()
    plt.title('quat_w')
    plt.xlabel('Timestamp')
    plt.ylabel('Quaternion')
    plt.plot(opti_timestamps, opti_quat_w, label='opti')
    plt.plot(vicon_timestamps, vicon_quat_w, label='vicon')
    plt.legend()

    plt.show()
