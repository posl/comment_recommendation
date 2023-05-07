def main():
    N, P = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] < P:
            ans += 1
    print(ans)
