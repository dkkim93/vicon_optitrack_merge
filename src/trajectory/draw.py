import matplotlib.pyplot as plt
import seaborn as sns

class Draw(object):
    def __init__(self):
        dummy = 1

    def draw_plot(self, vicon_ts, vicon_data, opti_ts, opti_data, T_ts, T_data,
                  title, xlabel, ylabel, vicon_legend, opti_legend, T_legend):
        plt.figure()
        plt.title(title, fontsize=18)
        plt.plot(vicon_ts, vicon_data, label=vicon_legend)
        plt.plot(opti_ts, opti_data, label=opti_legend)
        if T_ts is not None and T_data is not None: 
            plt.plot(T_ts, T_data, 'o', label=T_legend)
        plt.xlabel(xlabel, fontsize=12)
        plt.ylabel(ylabel, fontsize=12)
        plt.legend()

