#Problem Statement
#You are given an integer N and a sequence A=(A_1,A_2,…,A_N) of length N.
#Given Q queries, process them in the given order. Each query is of one of the following two kinds:
#1 k x : set the value A_k to x.
#2 k : print the value A_k.
#
#Constraints
#1≤N≤10^5
#1≤Q≤10^5
#0≤A_i≤10^9 (1≤i≤N)
#1≤k≤N for all queries.
#0≤x≤10^9 for all queries of the first kind.
#There is at least one query of the second kind.
#All values in the input are integers.
#
#Input
#The input is given from Standard Input in the following format:
#N
#A_1 A_2 … A_N
#Q
#query_1
#query_2
#⋮
#query_Q
#Here, query_i denotes the i-th query, given in one of the following formats:
#1 k x
#2 k
#
#Output
#Print q lines, where q is the number of queries of the second kind. The j-th (1≤j≤q) line should contain the response to the j-th such query.
#
#Sample Input 1
#3
#1 3 5
#7
#2 2
#2 3
#1 3 0
#2 3
#1 2 8
#2 2
#2 1
#
#Sample Output 1
#3
#5
#0
#8
#1
#
#Sample Input 2
#5
#22 2 16 7 30
#10
#1 4 0
#1 5 0
#2 2
#2 3
#2 4
#2 5
#1 4 100
#1 5 100
#2 3
#2 4
#
#Sample Output 2
#2
#16
#0
#0
#16
#100
#
#Sample Input 3
#7
#478 369 466 343 541 42 165
#20
#2 1
#1 7 729
#1 6 61
#1 6 838
#1 3 319
#1 4 317
#2 4
#1 1 673
#1 3 176
#1 5 250
#1 1 468
#2 6
#1 7 478
#1 5 595
#2 6
#1 6 599
#1 6 505
#2 3
#2 5
#2 1
#
#Sample Output 3
#478
#317
#838
#838
#176
#595
#468

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A[query[1]-1] = query[2]
        else:
            print(A[query[1]-1])

if __name__ == '__main__':
    main()