#Problem Statement
#Print all non-negative integers less than or equal to N in descending order.
#
#Constraints
#1≤N≤100
#N is an integer.
#
#Input
#The input is given from Standard Input in the following format:
#N
#
#Output
#Print X lines, where X is the number of non-negative integers less than or equal to N.
#For each i=1,2,…,X, the i-th line should contain the i-th greatest non-negative integer less than or equal to N.
#
#Sample Input 1
#3
#
#Sample Output 1
#3
#2
#1
#0
#
#Sample Input 2
#22
#
#Sample Output 2
#22
#21
#20
#19
#18
#17
#16
#15
#14
#13
#12
#11
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1
#0

def main():
    n = int(input())
    for i in range(n, -1, -1):
        print(i)

if __name__ == '__main__':
    main()