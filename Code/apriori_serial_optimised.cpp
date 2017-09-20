/* Serial Code for apriori algorithm */
#include "bits/stdc++.h"  	//includes all the usual c++ header files
#include <omp.h>

using namespace std;		//using the standard namespace

//macros
#define structure map<vector<int>, int>
#define FOR_MAP(ii,T) for(structure::iterator (ii)=(T).begin();(ii)!=(T).end();(ii)++)
#define FOR_next_MAP(jj,ii,T) for(structure::iterator (jj)=(ii);(jj)!=(T).end();(jj)++)
#define VI vector<int>

int MIN_SUP;
int flag = 0;			//set flag to 1 to print steps

structure C;
structure L;

void C1(string);
void L1();
void generate_C();
void generate_L();
void output(structure );
void scan_D(string);
void prune();
bool check_compatibility(VI ,VI );
void set_count(VI );

int main(int argc, char const *argv[])
{
MIN_SUP = atoi(argv[1]);			//min support count
int l = atoi(argv[2]);				//no of transactions
string file_name = argv[3];                     //filename

double start,end,time;

start = omp_get_wtime();
	
	C.clear();
	L.clear();

	bool mv=true;
	int index=2;
	while(true)
	{
		if (mv)
		{
			C1(file_name);
			if(flag)			
				{cout<<"C1\n";
				output(C);}

			L1();

			if(flag)			
				{cout<<"L1\n";
				output(L);
				}
			mv=!mv;
		}else
		{
			generate_C();
			if(C.size()==0)
				break;
			if(flag)			
				{cout<<"\nC"<<index<<"\n";
				output(C);}
			prune();
			if (C.size()==0)
			{
				break;
			}
	
			if(flag)			
				{cout<<"\nC"<<index<<" after prune \n";
				output(C);}

			scan_D(file_name);

			if(flag)	
				{cout<<"\nC"<<index<<"after scaning dataset \n";
				output(C);}
			generate_L();
			if (L.size()==0)
			{
				break;
			}
		
			if(flag)
				{cout<<"\nL"<<index<<"\n";
				output(L);}
		
			index++;
		}
	}
end = omp_get_wtime();
time = end - start;
cout<<""<<time<<"\n";
//cout<<"the time required is : "<<time<<"\n";
//cout<<"no of iterations : "<<index<<"\n";
return 0;
}

/* Generating the first candidate list */
void C1(string file_name)
{
	ifstream fin;
	fin.open(file_name.c_str());
	if(!fin)
		{
			cout<<"Input file opening error\n";
			exit(0);
		}

	int n;
	VI v;
	while(fin>>n)
	{
		v.clear();
		if (n==-1)            // -1 indicates end of line (transaction)
		{
			continue;
		}
		v.push_back(n);
		if(C.count(v)>0)
			C[v]++;
		else
			C[v]=1;
	}
	fin.close();
}

/* Prints all the candidates or frequency list along with their count */
void output(structure T)
{
	cout<<"\n";
	VI v;
	FOR_MAP(ii,T)
	{
		v.clear();
		v=ii->first;
		for (int i = 0; i < v.size(); ++i)
		{
			cout<<v[i]<<" ";
		}
		if(flag)
			{cout<<" ---(frequency)----->> "<<ii->second;
			cout<<"\n";}
	}
}

/* Generating the first frequency list */
void L1()
{

	FOR_MAP(ii,C)
	{
		if (ii->second >= MIN_SUP)
		{
			L[ii->first]=ii->second;
		}
	}

}

/* Generating all the cadidates of size k from frequency list of size k-1 */
void generate_C()
{
	//clean(C);
	C.clear();
	FOR_MAP(ii,L)
	{

		FOR_next_MAP(jj,ii,L)
		{
			if(jj==ii)
				continue;
			VI a,b;
			a.clear();
			b.clear();
			a=ii->first;
			b=jj->first;
			if(check_compatibility(a,b))	
			{
				a.push_back(b.back());
				sort(a.begin(), a.end());
				C[a]=0;
			}
		}

	}


}

/* Checking if any two frequency item sets are same or not */
bool check_compatibility(VI a,VI b)
{
	bool compatible=true;
	for (int i = 0; i < a.size()-1; ++i)
	{
		if (a[i]!=b[i])
		{
			compatible=false;
			break;
		}
	}

	return compatible;
}

/* Removing all the candidates of size k whose subsets of size k-1 are not in the frequency list of size k-1 */
void prune()
{
	VI a,b;
	
	FOR_MAP(ii,C)
	{
		a.clear();
		b.clear();

		a=ii->first;
		for(int i = 0;i<a.size();i++)
		{
			b.clear();
			for (int j = 0; j < a.size(); ++j)
			{
				if(j==i)                       
					continue;               
				b.push_back(a[j]);              // all the subsets are generated one by one and stored in b
			}
			if(L.find(b)==L.end())                  // check if subset exists in frequency item-set
				{
					ii->second=-1;
					break;
				}
			
		}

		
	}

	structure temp;
	temp.clear();
	FOR_MAP(ii,C)
	{
		if (ii->second != -1)
		{
			temp[ii->first]=ii->second;
		}
	}
	
	C.clear();
	C=temp;
	temp.clear();
}

/* Scanning the database and calling set_count for each transaction */
void scan_D(string file_name)
{
	ifstream fin;
	fin.open(file_name.c_str());
	if(!fin)
		{
			cout<<"Input file opening error\n";
			exit(0);
		}

	int n;
	VI a;
	while(fin>>n)
	{
		if(n==-1 && a.size()>0)
		{
			set_count(a);
			a.clear();
		}else if(n!=-1)
		{
			a.push_back(n);
		}
		
	}
	fin.close();
}

/* Incrementing the count of the candidate if it exists in the transaction, it is done for all candidates */
void set_count(VI a)
{
	FOR_MAP(ii,C)
	{
		VI b;
                b.clear();
                b=ii->first;
                int x;
                int true_count=0;
                int prev=-1;
                if (b.size()<=a.size())
                {
                        for (int i = 0; i < b.size(); ++i)
                        {
                                for (int j = prev+1; j < a.size(); ++j)  // Number of iterations of inner loop can be decreased based on the previous iteration result
                                {
                                        if(b[i]==a[j])
                                        {
                                                true_count++;
                                                prev = j;
                                                break;
                                        }
                                }
                        }
                }




		if (true_count==b.size())
		{
			ii->second++;
		}
	}
}

/* Finding the frequent item-sets of size k by removing all candidate item-sets having their count less than minimum support count */
void generate_L()
{
	L.clear();

	FOR_MAP(ii,C)
	{
		if(ii->second >= MIN_SUP)
		{
			L[ii->first]=ii->second;
		}
	}
}
