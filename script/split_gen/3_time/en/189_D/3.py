def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 1
    for s in S:
        ans *= 2 if s == "OR" else 1
    print(ans)
