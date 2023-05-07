def main():
    N, M = map(int, input().split())
    # 隣接リスト
    neighbors = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        neighbors[a-1].append(b-1)
        neighbors[b-1].append(a-1)
    # 連結成分の数を数える
    visited = [False] * N
    count = 0
    for i in range(N):
        if visited[i]:
            continue
        count += 1
        stack = [i]
        while stack:
            j = stack.pop()
            if visited[j]:
                continue
            visited[j] = True
            stack.extend(neighbors[j])
    # 連結成分の数が 1 なら Yes
    print('Yes' if count == 1 else 'No')
