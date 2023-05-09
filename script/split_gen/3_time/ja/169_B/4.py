def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 1
    for i in range(n):
        if a[i] == 0:
            print(0)
            exit()
        if ans > 10 ** 18 // a[i]:
            print(-1)
            exit()
        ans *= a[i]
    print(ans)
