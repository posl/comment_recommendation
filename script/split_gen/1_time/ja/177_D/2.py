def main():
    N, M = map(int, input().split())
    friends = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        friends[a-1].add(b-1)
        friends[b-1].add(a-1)
    group = [0] * N
    group_num = 0
    for i in range(N):
        if group[i] == 0:
            group_num += 1
            group[i] = group_num
            stack = [i]
            while stack:
                now = stack.pop()
                for j in friends[now]:
                    if group[j] == 0:
                        group[j] = group_num
                        stack.append(j)
    print(group_num)
