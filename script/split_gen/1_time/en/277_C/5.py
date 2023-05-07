def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    N = int(input())
    ladder = []
    for _ in range(N):
        A, B = map(int, input().split())
        ladder.append((min(A, B), max(A, B)))
    ladder.sort(key=lambda x: x[0])
    max_floor = ladder[-1][1]
    ladder_dict = defaultdict(list)
    for A, B in ladder:
        ladder_dict[A].append(B)
    dp = [0] * (max_floor + 1)
    for i in range(1, max_floor + 1):
        if i in ladder_dict:
            for j in ladder_dict[i]:
                dp[j] = max(dp[j], dp[i] + 1)
    print(dp[-1])
