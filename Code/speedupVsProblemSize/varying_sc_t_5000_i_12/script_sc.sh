#!/bin/sh
#echo "running apriori serially as well as parallely"
#sizes[0]=262144 		#4096*64 
#sizes[1]=2097152 		#4096*512 
#sizes[2]=16777216		#4096*4096
#sizes[3]=134217728		#4096*4096*8
#sizes[4]=1073741824		#4096*4096*8*8
#sizes[5]=8589934592		#4096*4096*8*8*8		

sc[0]=50
sc[1]=100 		 
sc[2]=200		
sc[3]=500		
sc[4]=700		
sc[5]=1000
sc[6]=1200	
sc[7]=1500
sc[8]=1800
sc[9]=2000
				
i=0
threads=16
m=1
trans=5000
items=12
filename="input1.txt"

       #gcc -Wall reduction_serial2.c -fopenmp -lm
       #./a.out ${sizes[i]}  


while [ $i -lt 10 ]
do
	#echo "for serial " ${sc[i]}
	g++ apriori.cpp -fopenmp
	./a.out ${sc[i]} $trans $filename	

       #echo "for parallel " ${sc[i]}
       g++ apriori_parallel.cpp -fopenmp
       ./a.out ${sc[i]} $trans $threads $filename
	
	i=`expr $i \+ $m`
done	
