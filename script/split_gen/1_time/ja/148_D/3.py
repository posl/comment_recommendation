def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if a[i-1] == i:
            ans += 1
            a[i-1] = 0
            a[i] = 0
    if a[N-1] == N:
        ans += 1
    print(N-ans)
