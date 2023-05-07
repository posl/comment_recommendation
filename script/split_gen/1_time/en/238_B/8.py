def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    res = 0
    for a in A:
        res = (a + res + 1) // 2 * 2
    print(res)
