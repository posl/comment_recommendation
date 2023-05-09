def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.sort()
    for i in range(1,N+1):
        if A[i-1] != i:
            print('No')
            return
    print('Yes')
