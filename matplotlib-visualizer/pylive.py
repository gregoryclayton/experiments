import matplotlib.pyplot as plt
import numpy as np

def live_plotter(x_vec,y1_data,line1,pause_time=0.005):
    if line1==[]:
       
        plt.ion()
        fig = plt.figure(figsize=(13,6))
        ax = fig.add_subplot(111)
    
        line1, = ax.plot(x_vec,y1_data,'-x',alpha=0.4)        
        
        plt.show()
    
    line1.set_ydata(y1_data)
   
    if np.min(y1_data)<=line1.axes.get_ylim()[0] or np.max(y1_data)>=line1.axes.get_ylim()[1]:
        plt.ylim([np.min(y1_data)-np.std(y1_data),np.max(y1_data)+np.std(y1_data)])

    plt.pause(pause_time)
    
    return line1