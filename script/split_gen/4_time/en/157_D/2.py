def main():
    N, M, K = map(int, input().split())
    friends = []
    blocks = []
    for _ in range(M):
        friends.append(list(map(int, input().split())))
    for _ in range(K):
        blocks.append(list(map(int, input().split())))
    answer = [0] * N
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if i == j:
                continue
            if [i, j] in friends:
                continue
            if [j, i] in friends:
                continue
            if [i, j] in blocks:
                continue
            if [j, i] in blocks:
                continue
            answer[i - 1] += 1
    print(*answer)
