import matplotlib.pyplot as plt

with open('/home/amartya/Desktop/Codes/Assignment 2/Q2/output.txt', 'r') as f:
    times = [float(line.split()[-1]) for line in f]
colors = ['red', 'green', 'blue']
x=["Other","RR","FIFO"]
bar_width=[1,1,1]
plt.bar(x, times, width=bar_width, color=colors)
plt.ylabel('Time to complete')
plt.xlabel('Scheduling policies')
plt.show()

"""
colors = ['red', 'green', 'blue']
plt.hist(times, color=colors, bins=3, rwidth=0.8)
plt.ylabel('Time to complete (in seconds)')
plt.xlabel('Scheduling policies')
plt.show()

plt.hist(times[0],times[1],times[2], bins=3,color=['red',"green","blue"])
    ##, 'green', 'blue'])
plt.xlabel('Time to complete')
plt.ylabel('Scheduling priorities')
plt.show()
"""