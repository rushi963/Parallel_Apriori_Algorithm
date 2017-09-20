#this python script is used to read execution times for serial and parallel executions for varying problem sizes and plot them as well as the speedup.
#the format of the input text file is as follows : each input size corresponds to 2 lines - 
#1st line - serial time.
#2nd line - parallel time.
#the input text file is made by using a bash script named script2.sh.

import matplotlib.pyplot as plt

sizes = [50,100,200,500,700,1000,1200,1500,1800,2000]
#sizes = [2**20,2**21,2**22,2**23,2**24,2**25,2**26,2**27,2**28]
#x_ticks = [2**20,2**21,2**22,2**23,2**24,2**25,2**26,2**27,2**28]
x_ticks = [50,100,200,500,700,1000,1200,1500,1800,2000]

file = open('threads_2.txt')	#change file name accordingly.
speedup1 = []
st1 = []
pt1 = []
for i in range(10):
	serialTime = (float)(file.readline())
	parallelTime = (float)(file.readline())
	speedUp = serialTime/parallelTime;
	st1.append(serialTime)
	pt1.append(parallelTime)	
	speedup1.append(speedUp)

file = open('threads_4.txt')	#change file name accordingly.
speedup2 = []
st2 = []
pt2 = []
for i in range(10):
	serialTime = (float)(file.readline())
	parallelTime = (float)(file.readline())
	speedUp = serialTime/parallelTime;
	st2.append(serialTime)
	pt2.append(parallelTime)	
	speedup2.append(speedUp)

file = open('threads_6.txt')	#change file name accordingly.
speedup3 = []
st3 = []
pt3 = []
for i in range(10):
	serialTime = (float)(file.readline())
	parallelTime = (float)(file.readline())
	speedUp = serialTime/parallelTime;
	st3.append(serialTime)
	pt3.append(parallelTime)	
	speedup3.append(speedUp)
	

file = open('threads_8.txt')	#change file name accordingly.
speedup4 = []
st4 = []
pt4 = []
for i in range(10):
	serialTime = (float)(file.readline())
	parallelTime = (float)(file.readline())
	speedUp = serialTime/parallelTime;
	st4.append(serialTime)
	pt4.append(parallelTime)	
	speedup4.append(speedUp)


file = open('threads_10.txt')	#change file name accordingly.
speedup5 = []
st5 = []
pt5 = []
for i in range(10):
	serialTime = (float)(file.readline())
	parallelTime = (float)(file.readline())
	speedUp = serialTime/parallelTime;
	st5.append(serialTime)
	pt5.append(parallelTime)	
	speedup5.append(speedUp)


plt.figure(0);
plt.xticks(sizes,x_ticks)
plt.plot(sizes,speedup1,label = '2 threads')
plt.plot(sizes,speedup2,label = '4 threads')
plt.plot(sizes,speedup3,label = '6 threads')
plt.plot(sizes,speedup4,label = '8 threads')
plt.plot(sizes,speedup5,label = '10 threads')
plt.legend(loc = 'upper left')
plt.ylabel('speedup')
#plt.ylim(0,8)
#plt.xscale('log')
plt.xlabel('support count')
plt.title('speedup vs support count(t=5000,i=12)')
plt.figure();
plt.show();

plt.figure(1);
plt.xticks(sizes,x_ticks)
plt.plot(sizes,st1,label = 'serial')
plt.plot(sizes,pt1,label = 'parallel_2_threads')
plt.plot(sizes,pt2,label = 'parallel_4_threads')
plt.plot(sizes,pt3,label = 'parallel_6_threads')
plt.plot(sizes,pt4,label = 'parallel_8_threads')
plt.plot(sizes,pt5,label = 'parallel_10_threads')
plt.legend(loc = 'upper left')
#plt.xscale('log')
plt.ylabel('time required in sec')
plt.xlabel('support count')
plt.title('Time required vs support count(t=5000,i=12)')
plt.show()


