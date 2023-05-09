def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, N):
        if a[i] > a[i-1] + 1:
            break
        ans += 1
    print(ans)
