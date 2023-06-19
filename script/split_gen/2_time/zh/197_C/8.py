def main():
    N = int(input())
    A = list(map(int, input().split()))
    res = 2**30
    for i in range(N):
        t = A[i]
        for j in range(i, N):
            t = t | A[j]
            res = min(res, t)
    print(res)
