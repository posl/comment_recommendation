def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A = [a % 200 for a in A]
    mod = [0] * 200
    for a in A:
        mod[a] += 1
    ans = 0
    for m in mod:
        if m > 1:
            ans += m * (m - 1) // 2
    print(ans)
