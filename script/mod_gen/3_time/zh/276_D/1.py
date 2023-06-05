def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        flag = True
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] = a[i] / 2
            elif a[i] % 3 == 0:
                a[i] = a[i] / 3
            else:
                flag = False
                break
        if flag:
            ans += 1
        else:
            break
    for i in range(n):
        if a[i] != a[0]:
            print(-1)
            exit()
    print(ans)

if __name__ == '__main__':
    solve()