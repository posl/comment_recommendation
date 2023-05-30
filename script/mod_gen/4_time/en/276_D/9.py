def d():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while True:
        if all(map(lambda x: x % 2 == 0, a)):
            a = list(map(lambda x: x / 2, a))
            ans += 1
        else:
            break
    print(ans)
d()
