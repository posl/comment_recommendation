def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if a[i] <= i + 1:
            continue
        else:
            ans += 1
    print(ans)
