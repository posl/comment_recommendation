def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    for i in range(N):
        ans[i] += (K // N)
    K %= N
    for i in range(K):
        ans[i] += 1
    for i in range(N):
        print(ans[bisect_left(a, i + 1) - 1])
