def main():
    n = int(input())
    a = list(map(int, input().split(" ")))
    ans = 0
    for i in range(n-1, 0, -1):
        if a[i] - a[i-1] >= 2:
            print(-1)
            exit()
        elif a[i] - a[i-1] == 1:
            ans += 1
        else:
            ans += a[i]
    ans += a[0]
    print(ans)
