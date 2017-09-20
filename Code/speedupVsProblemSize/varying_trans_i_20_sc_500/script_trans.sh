#!/bin/sh
#echo "running apriori serially as well as parallely"
#sizes[0]=262144 		#4096*64 
#sizes[1]=2097152 		#4096*512 
#sizes[2]=16777216		#4096*4096
#sizes[3]=134217728		#4096*4096*8
#sizes[4]=1073741824		#4096*4096*8*8
#sizes[5]=8589934592		#4096*4096*8*8*8		

trans[0]=1000
trans[1]=2000 		 
trans[2]=3000		
trans[3]=4000		
trans[4]=5000		
trans[5]=6000
trans[6]=7000
trans[7]=8000

filename[0]=trans_1000_items_20.txt
filename[1]=trans_2000_items_20.txt
filename[2]=trans_3000_items_20.txt
filename[3]=trans_4000_items_20.txt
filename[4]=trans_5000_items_20.txt
filename[5]=trans_6000_items_20.txt
filename[6]=trans_7000_items_20.txt
filename[7]=trans_8000_items_20.txt				

i=0
threads=16
m=1
sc=500
items=20

       #gcc -Wall reduction_serial2.c -fopenmp -lm
       #./a.out ${sizes[i]}  


while [ $i -lt 8 ]
do
	#echo "for serial " ${sc[i]}
	g++ apriori.cpp -fopenmp
	./a.out $sc ${trans[i]} ${filename[i]}  	

       #echo "for parallel " ${sc[i]}
       g++ apriori_parallel.cpp -fopenmp
       ./a.out $sc ${trans[i]} $threads ${filename[i]}
	
	i=`expr $i \+ $m`
done	
