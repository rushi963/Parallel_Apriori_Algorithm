#this python script is used to read execution times for parallel executions for varying number of cores and plot the speedup.

import matplotlib.pyplot as plt

file1 = open('output_t_5000_i_10_sc_1000.txt')
cores = [2,4,6,8,10]
speedup1 = []
x_ticks = [2,4,6,8,10]
efficiency1 = []
serialTime1 = (float)(file1.readline())

for i in range(5):
	parallelTime = (float)(file1.readline())
	speedUp = serialTime1/parallelTime;
	speedup1.append(speedUp)
	efficiency1.append(speedUp/(2*i+2))

file2 = open('output_t_5000_i_15_sc_1000.txt')
speedup2 = []
efficiency2 = []
serialTime2 = (float)(file2.readline())


for i in range(5):
	parallelTime = (float)(file2.readline())
	speedUp = serialTime2/parallelTime;
	speedup2.append(speedUp)
	efficiency2.append(speedUp/(2*i+2))

file3 = open('output_t_5000_i_20_sc_1000.txt')
speedup3 = []
efficiency3 = []
serialTime3 = (float)(file3.readline())


for i in range(5):
	parallelTime = (float)(file3.readline())
	speedUp = serialTime3/parallelTime;
	speedup3.append(speedUp)
	efficiency3.append(speedUp/(2*i+2))

plt.figure(0);
plt.xticks(cores,x_ticks)
plt.plot(cores,speedup1,label="i = 10")
plt.plot(cores,speedup2,label="i = 15")
plt.plot(cores,speedup3,label="i = 20")
#plt.plot(cores,speedup6,label="support count = 1000")

plt.legend(loc = 'upper left')
plt.ylabel('speedup')
plt.xlabel('no of cores')
plt.title('speedup vs no of cores(sc=1000,t=5000)')
plt.figure();
plt.show();


plt.figure(1);
plt.xticks(cores,x_ticks)
plt.plot(cores,efficiency1,label = "i = 10")
plt.plot(cores,efficiency2,label = "i = 15")
plt.plot(cores,efficiency3,label = "i = 20")
#plt.plot(cores,efficiency6,label = "support count = 1000")

plt.legend(loc = 'upper left')
plt.ylabel('efficiency')
plt.xlabel('no of cores')
plt.ylim(0.2,1)
plt.title('efficiency vs no of cores(sc=1000,t=5000)')
plt.show();


