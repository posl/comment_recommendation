def main():
    N, M, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    CD = [list(map(int, input().split())) for _ in range(K)]
    # 人iの友達の数
    friends = [0] * (N + 1)
    # 人iのブロックの数
    blocks = [0] * (N + 1)
    for a, b in AB:
        friends[a] += 1
        friends[b] += 1
    for c, d in CD:
        blocks[c] += 1
        blocks[d] += 1
    result = [0] * (N + 1)
    for i in range(1, N + 1):
        result[i] = friends[i] - blocks[i] - 1
    print(*result[1:])
