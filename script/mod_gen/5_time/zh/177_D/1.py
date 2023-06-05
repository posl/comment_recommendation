def main():
    N, M = map(int, input().split())
    friends = [[] for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        friends[a - 1].append(b - 1)
        friends[b - 1].append(a - 1)
    # print(friends)
    group = [0] * N
    group_num = 0
    for i in range(N):
        if group[i] == 0:
            group_num += 1
            group[i] = group_num
            stack = [i]
            while stack:
                j = stack.pop()
                for k in friends[j]:
                    if group[k] == 0:
                        group[k] = group_num
                        stack.append(k)
    print(group_num)

if __name__ == '__main__':
    main()