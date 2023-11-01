def main():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    A.sort(reverse=True)
    sum = 0
    for i in range(N):
        sum += A[i]
    for i in range(M):
