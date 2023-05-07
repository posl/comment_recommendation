def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 2 ** N
    if S[-1] == "AND":
        ans -= 2 ** (N - 1)
    print(ans)
