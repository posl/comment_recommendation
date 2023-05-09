def main():
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    alpha = [0] * 26
    for s in S:
        for c in s:
            alpha[ord(c) - ord('a')] += 1
    alpha.sort(reverse=True)
    print(sum(alpha[:K]))
