def main():
    N = int(input())
    road = [[] for _ in range(N)]
    for _ in range(N-1):
        A,B = map(int,input().split())
        road[A-1].append(B-1)
        road[B-1].append(A-1)
    #print(road)
    stack = [0]
    visited = [False]*N
    visited[0] = True
    while stack:
        v = stack.pop()
        print(v+1,end=' ')
        for i in road[v]:
            if visited[i]:
                continue
            visited[i] = True
            stack.append(v)
            stack.append(i)
            break
    print()
    return

if __name__ == '__main__':
    main()