def main():
    #input
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    #calc
    A.sort()
    A.reverse()
    sum_A = sum(A)
    if A[M-1] >= sum_A/(4*M):
        print('Yes')
    else:
        print('No')
    #output
