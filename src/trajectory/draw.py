import matplotlib.pyplot as plt
import seaborn as sns

class Draw(object):
    def __init__(self):
        dummy = 1

    def draw_plot(self, vicon_ts, vicon_data, opti_ts, opti_data,
                  title, xlabel, ylabel, vicon_legend, opti_legend):
        plt.figure()
        plt.title(title)
        plt.plot(vicon_ts, vicon_data, label=vicon_legend)
        plt.plot(opti_ts, opti_data, label=opti_legend)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend()

