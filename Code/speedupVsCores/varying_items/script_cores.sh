#!/bin/sh
#this script is for speedup vs no of cores graph
#echo "running apriori serially as well as parallely"
#sizes[0]=262144 		#4096*64 
#sizes[1]=2097152 		#4096*512 
#sizes[2]=16777216		#4096*4096
#sizes[3]=134217728		#4096*4096*8
#sizes[4]=1073741824		#4096*4096*8*8
#sizes[5]=8589934592		#4096*4096*8*8*8		

#trans[0]=1000
#trans[1]=2000 		 
#trans[2]=3000		
#trans[3]=4000		
#trans[4]=5000		
#trans[5]=6000
#trans[6]=7000
#trans[7]=8000

filename[1]=trans_5000_items_5.txt
filename[2]=trans_5000_items_10.txt
filename[3]=trans_5000_items_15.txt
filename[4]=trans_5000_items_20.txt

output_file[1]=output_t_5000_i_5_sc_1000.txt
output_file[2]=output_t_5000_i_10_sc_1000.txt
output_file[3]=output_t_5000_i_15_sc_1000.txt
output_file[4]=output_t_5000_i_20_sc_1000.txt
#output_file[5]=output_t_5000_i_20_sc_50.txt
#output_file[6]=output_t_6000_i_20_sc_50.txt
#output_file[7]=output_t_7000_i_20_sc_50.txt

#filename[1]=trans_5000_items_10.txt
#filename[2]=trans_5000_items_15.txt
#filename[3]=trans_5000_items_20.txt
#filename[4]=trans_5000_items_25.txtit
#filename[5]=trans_5000_items_30.txt
#filename[6]=trans_5000_items_35.txt
#filename[7]=trans_5000_items_40.txt				

threads=2	
m=2
#incr=5
incr1=1
iter=1
sc=1000
trans=5000

while [ $iter -lt 5 ]
do
       g++ apriori.cpp -fopenmp
	./a.out $sc $trans ${filename[iter]} > ${output_file[iter]}

threads=2	
while [ $threads -lt 17 ]
do
       g++ apriori_parallel.cpp -fopenmp
       ./a.out $sc $trans $threads ${filename[iter]} >> ${output_file[iter]}
	threads=`expr $threads \+ $m`
done
iter=`expr $iter \+ $incr1`
#trans=`expr $trans \+ $incr`
done
