#Problem Statement
#You observed amoebae and kept some records.
#Initially, there was one amoeba, numbered 1.
#You made N records. According to the i-th record, the amoeba numbered A_i disappeared by dividing itself into two new amoebae, which were then numbered 2i and 2i+1.
#Here, amoeba A_i is said to be the parent of amoebae 2i and 2i+1.
#For each k=1,...,2N+1, how many generations away is amoeba k from amoeba 1?
#
#Constraints
#1 ≦ N ≦ 2× 10^5
#The records are consistent. That is:
#1≦ A_i ≦ 2i-1.
#A_i are distinct integers.
#
#
#Input
#The input is given from Standard Input in the following format:
#N
#A_1 A_2 ... A_N
#
#Output
#Print 2N+1 lines. The k-th line should contain the generation distance between amoeba 1 and amoeba k.
#
#Sample Input 1
#2
#1 2
#
#Sample Output 1
#0
#1
#1
#2
#2
#From amoeba 1, amoebae 2 and 3 were born. From amoeba 2, amoebae 4 and 5 were born.
#Amoeba 1 is zero generations away from amoeba 1.
#Amoeba 2 is one generation away from amoeba 1.
#Amoeba 3 is one generation away from amoeba 1.
#Amoeba 4 is one generation away from amoeba 2, and two generations away from amoeba 1.
#Amoeba 5 is one generation away from amoeba 2, and two generations away from amoeba 1.
#
#Sample Input 2
#4
#1 3 5 2
#
#Sample Output 2
#0
#1
#1
#2
#2
#3
#3
#2
#2

def 