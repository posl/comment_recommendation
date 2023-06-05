def solution():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for a in A:
        if ans < a:
            break
        ans += a
    print(ans)
solution()
