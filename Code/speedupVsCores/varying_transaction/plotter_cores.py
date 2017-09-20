#this python script is used to read execution times for parallel executions for varying number of cores and plot the speedup.

import matplotlib.pyplot as plt

file1 = open('output_t_1000_i_20_sc_500.txt')
cores = [2,4,6,8,10,12,14,16]
speedup1 = []
x_ticks = [2,4,6,8,10,12,14,16]
efficiency1 = []
serialTime1 = (float)(file1.readline())

for i in range(8):
	parallelTime = (float)(file1.readline())
	speedUp = serialTime1/parallelTime;
	speedup1.append(speedUp)
	efficiency1.append(speedUp/(2*i+2))

file2 = open('output_t_2000_i_20_sc_500.txt')
speedup2 = []
efficiency2 = []
serialTime2 = (float)(file2.readline())


for i in range(8):
	parallelTime = (float)(file2.readline())
	speedUp = serialTime2/parallelTime;
	speedup2.append(speedUp)
	efficiency2.append(speedUp/(2*i+2))

file3 = open('output_t_3000_i_20_sc_500.txt')
speedup3 = []
efficiency3 = []
serialTime3 = (float)(file3.readline())


for i in range(8):
	parallelTime = (float)(file3.readline())
	speedUp = serialTime3/parallelTime;
	speedup3.append(speedUp)
	efficiency3.append(speedUp/(2*i+2))

file4 = open('output_t_4000_i_20_sc_500.txt')
speedup4 = []
efficiency4 = []
serialTime4 = (float)(file4.readline())


for i in range(8):
	parallelTime = (float)(file4.readline())
	speedUp = serialTime4/parallelTime;
	speedup4.append(speedUp)
	efficiency4.append(speedUp/(2*i+2))

file5 = open('output_t_5000_i_20_sc_500.txt')
speedup5 = []
efficiency5 = []
serialTime5 = (float)(file5.readline())


for i in range(8):
	parallelTime = (float)(file5.readline())
	speedUp = serialTime5/parallelTime;
	speedup5.append(speedUp)
	efficiency5.append(speedUp/(2*i+2))


plt.figure(0);
plt.xticks(cores,x_ticks)
plt.plot(cores,speedup1,label="t = 1000")
plt.plot(cores,speedup2,label="t = 2000")
plt.plot(cores,speedup3,label="t = 3000")
plt.plot(cores,speedup4,label="t = 4000")
plt.plot(cores,speedup5,label="t = 5000")
#plt.plot(cores,speedup6,label="support count = 1000")

plt.legend(loc = 'upper left')
plt.ylabel('speedup')
plt.xlabel('no of cores')
plt.title('speedup vs no of cores(sc=500,i=20)')
plt.figure();
plt.show();


plt.figure(1);
plt.xticks(cores,x_ticks)
plt.plot(cores,efficiency1,label = "t = 1000")
plt.plot(cores,efficiency2,label = "t = 2000")
plt.plot(cores,efficiency3,label = "t = 3000")
plt.plot(cores,efficiency4,label = "t = 4000")
plt.plot(cores,efficiency5,label = "t = 5000")
#plt.plot(cores,efficiency6,label = "support count = 1000")

plt.legend(loc = 'upper left')
plt.ylabel('efficiency')
plt.xlabel('no of cores')
plt.ylim(0,1)
plt.title('efficiency vs no of cores(sc=500,i=20)')
plt.show();


