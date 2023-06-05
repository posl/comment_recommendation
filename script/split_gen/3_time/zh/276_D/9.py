def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        flag = False
        for i in range(n):
            if a[i] % 2 == 0:
                a[i] //= 2
                flag = True
                ans += 1
        if flag:
            continue
        for i in range(n):
            if a[i] % 3 == 0:
                a[i] //= 3
                flag = True
                ans += 1
        if flag:
            continue
        break
    for i in range(n):
        if a[i] != a[0]:
            print(-1)
            return
    print(ans)
