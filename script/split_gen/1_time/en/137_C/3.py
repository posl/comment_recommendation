def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = ["".join(sorted(s)) for s in S]
    from collections import Counter
    S = Counter(S)
    ans = 0
    for s in S.values():
        ans += s * (s - 1) // 2
    print(ans)
