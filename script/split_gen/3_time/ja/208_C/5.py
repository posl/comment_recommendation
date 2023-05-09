def main():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * N
    ans[0] = K // N
    K %= N
    for i in range(K):
        ans[a.index(i+1)] += 1
    for i in range(N):
        print(ans[i])
