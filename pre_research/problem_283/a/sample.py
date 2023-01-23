#Problem Statement
#Given integers A and B, print the value A^B.
#
#Constraints
#1≤A,B≤9
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#A B
#
#Output
#Print the answer.
#
#Sample Input 1
#4 3
#
#Sample Output 1
#64
#
#Sample Input 2
#5 5
#
#Sample Output 2
#3125
#
#Sample Input 3
#8 1
#
#Sample Output 3
#8

def main():
    A, B = map(int, input().split())
    print(A**B)

if __name__ == '__main__':
    main()