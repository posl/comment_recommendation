def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(map(abs, a))
    cnt = 0
    for i in a:
        if i < 0:
            cnt += 1
    if cnt % 2 == 0:
        print(s)
    else:
        print(s - 2 * min(map(abs, a)))
solve()
