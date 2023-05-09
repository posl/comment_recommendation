def main():
    N, K = map(int, input().split())
    ans = 0
    for _ in range(K):
        d = int(input())
        A = list(map(int, input().split()))
        ans += N - d
    print(ans)
