#this python script is used to read execution times for parallel executions for varying number of cores and plot the speedup.

import matplotlib.pyplot as plt

file1 = open('output_t_5000_i_12_sc_500.txt')
cores = [2,4,6,8]
speedup1 = []
x_ticks = [2,4,6,8]
efficiency1 = []
serialTime1 = (float)(file1.readline())

for i in range(4):
	parallelTime = (float)(file1.readline())
	speedUp = serialTime1/parallelTime;
	speedup1.append(speedUp)
	efficiency1.append(speedUp/(2*i+2))

file2 = open('output_t_5000_i_12_sc_1000.txt')
speedup2 = []
efficiency2 = []
serialTime2 = (float)(file2.readline())


for i in range(4):
	parallelTime = (float)(file2.readline())
	speedUp = serialTime2/parallelTime;
	speedup2.append(speedUp)
	efficiency2.append(speedUp/(2*i+2))

file3 = open('output_t_5000_i_12_sc_1500.txt')
speedup3 = []
efficiency3 = []
serialTime3 = (float)(file3.readline())


for i in range(4):
	parallelTime = (float)(file3.readline())
	speedUp = serialTime3/parallelTime;
	speedup3.append(speedUp)
	efficiency3.append(speedUp/(2*i+2))

plt.figure(0);
plt.xticks(cores,x_ticks)
plt.plot(cores,speedup1,label="support count = 500")
plt.plot(cores,speedup2,label="support count = 1000")
plt.plot(cores,speedup3,label="support count = 1500")

plt.legend(loc = 'upper left')
plt.ylabel('speedup')
plt.xlabel('no of cores')
plt.ylim(1,6)
plt.title('speedup vs no of cores(t=5000,i=12)')
plt.figure();
plt.show();


plt.figure(1);
plt.xticks(cores,x_ticks)
plt.plot(cores,efficiency1,label = "support count = 500")
plt.plot(cores,efficiency2,label = "support count = 1000")
plt.plot(cores,efficiency3,label = "support count = 1500")

plt.legend(loc = 'upper left')
plt.ylabel('efficiency')
plt.xlabel('no of cores')
plt.ylim(0,1)
plt.title('efficiency vs no of cores(t=5000,i=12)')
plt.show();



