def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    graph = [[] for i in range(N)]
    for i in range(N-1):
        graph[A[i]-1].append(B[i]-1)
        graph[B[i]-1].append(A[i]-1)
    ans = [1]
    visited = [False] * N
    visited[0] = True
    while len(ans) < N:
        for i in graph[ans[-1]-1]:
            if not visited[i]:
                ans.append(i+1)
                visited[i] = True
                break
        else:
            ans.append(ans[-2])
    print(*ans)
