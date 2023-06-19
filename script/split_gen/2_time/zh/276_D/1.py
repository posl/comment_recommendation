def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = 0
    while True:
        if all(x % 2 == 0 for x in A):
            A = [x // 2 for x in A]
            ans += 1
        else:
            break
    print(ans)
solve()
