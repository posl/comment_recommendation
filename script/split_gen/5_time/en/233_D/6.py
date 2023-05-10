def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    S = [0]
    for a in A:
        S.append(S[-1] + a)
    from collections import defaultdict
    D = defaultdict(int)
    ans = 0
    for s in S:
        ans += D[s]
        D[s + K] += 1
    print(ans)
