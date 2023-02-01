#Problem Statement
#You are given an integer K.
#Print a string that is a concatenation of the first K uppercase English letters in ascending order, starting from A.
#
#Constraints
#K is an integer between 1 and 26, inclusive.
#
#Input
#The input is given from Standard Input in the following format:
#K
#
#Output
#Print the answer.
#
#Sample Input 1
#3
#
#Sample Output 1
#ABC
#
#Sample Input 2
#1
#
#Sample Output 2
#A

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(65, 65 + K)]))

if __name__ == '__main__':
    main()