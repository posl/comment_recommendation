def problems161_b():
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(N):
        sum += A[i]
    if A[M-1] >= sum /(4*M):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    problems161_b()