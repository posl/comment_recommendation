def main():
    # input
    N = int(input())
    A = [int(x) for x in input().split()]
    # compute
    B = [[A[2*i], A[2*i+1]] for i in range(2**(N-1))]
    B.sort(key=lambda x:x[1])
    B.sort(key=lambda x:x[0])
    # output
    print(A.index(B[-2][1])+1)
