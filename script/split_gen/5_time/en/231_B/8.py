def solve():
    N = int(input())
    S = [input() for _ in range(N)]
    print(max(set(S), key = S.count))
