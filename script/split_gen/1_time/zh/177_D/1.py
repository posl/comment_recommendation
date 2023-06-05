def main():
    N, M = map(int, input().split())
    friend = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)
    group = [0] * N
    group_id = 1
    for i in range(N):
        if group[i] == 0:
            dfs(friend, group, i, group_id)
            group_id += 1
    print(max(group))
