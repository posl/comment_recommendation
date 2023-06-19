def main():
    n,m = map(int,input().split())
    friend = [[] for _ in range(n)]
    for _ in range(m):
        a,b = map(int,input().split())
        friend[a-1].append(b-1)
        friend[b-1].append(a-1)
    group = [-1]*n
    group[0] = 0
    stack = [0]
    while stack:
        i = stack.pop()
        for j in friend[i]:
            if group[j] == -1:
                group[j] = 1-group[i]
                stack.append(j)
            elif group[j] == group[i]:
                print(0)
                return
    print(group.count(0)*group.count(1)-m)
    return

if __name__ == '__main__':
    main()