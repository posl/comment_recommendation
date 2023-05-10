def solve():
    N, L = map(int, input().split())
    total = 0
    for i in range(N):
        total += L + i
    if L >= 0:
        print(total - L - N)
    elif L + N - 1 <= 0:
        print(total - L)
    else:
        print(total)
