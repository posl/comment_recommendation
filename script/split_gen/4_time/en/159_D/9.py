def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N, A)
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    #print(d)
    ans = 0
    for i in range(N):
        ans += d[A[i]] - 1
    for i in range(N):
        print(ans - d[A[i]] + 1)
