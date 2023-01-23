#Problem Statement
#You are given a positive integer N. It is known that N can be represented as N=p^2 q using two different prime numbers p and q.
#Find p and q.
#You have T test cases to solve.
#
#Constraints
#All values in the input are integers.
#1≤T≤10
#1≤N≤9×10^18
#N can be represented as N=p^2 q using two different prime numbers p and q.
#
#Input
#The input is given from Standard Input in the following format, where test_i represents the i-th test case:
#T
#test_1
#test_2 
#⋮
#test_T
#Each test case is in the following format:
#N
#
#Output
#Print T lines.
#The i-th (1≤i≤T) line should contain p and q for the i-th test case, separated by a space. Under the constraints of this problem, it can be proved that the pair of prime numbers 
#p and q such that N=p^2 q is unique.
#
#Sample Input 1
#3
#2023
#63
#1059872604593911
#
#Sample Output 1
#17 7
#3 7
#104149 97711

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        p = 1
        q = 1
        for i in range(2, int(N**0.5)+1):
            if N % i == 0:
                p = i
                q = N // i
                break
        print(p, q)

if __name__ == '__main__':
    main()