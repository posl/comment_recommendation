def solve():
    N = int(input())
    S = [input() for i in range(N)]
    print(2**N - (1 if "OR" in S else 0))
