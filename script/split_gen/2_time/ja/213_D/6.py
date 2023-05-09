def main():
    N = int(input())
    road = [[] for _ in range(N+1)]
    for _ in range(N-1):
        A,B = map(int,input().split())
        road[A].append(B)
        road[B].append(A)
    ans = [1]
    next = road[1]
    visited = [0]*(N+1)
    visited[1] = 1
    while next:
        next.sort()
        for n in next:
            if visited[n] == 0:
                ans.append(n)
                visited[n] = 1
                next = road[n]
                break
        else:
            next = road[ans[-2]]
    print(*ans)
