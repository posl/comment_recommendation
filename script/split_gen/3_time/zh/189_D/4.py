def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 1
    for s in S:
        if s == "OR":
            ans = ans * 2 + 1
        else:
            ans = ans * 2
    print(ans)
