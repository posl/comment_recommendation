def solve():
    A, B = map(int, input().split())
    ans = 1
    for i in range(A - B):
        ans *= 32
    print(ans)
