def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = []
    for i in range(1,N+1):
        B.append((A[i-1],i))
    B.sort()
    for i in range(N):
        print(B[i][1],end=' ')
