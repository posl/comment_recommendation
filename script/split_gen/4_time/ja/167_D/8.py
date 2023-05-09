def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = [False] * (N + 1)
    visited[1] = True
    # print(visited)
    # print(A)
    # print(A[0])
    # print(visited[A[0]])
    # print(visited[A[0]] == False)
    count = 0
    ans = 1
    while count < K:
        ans = A[ans - 1]
        if visited[ans] == False:
            visited[ans] = True
            count += 1
        else:
            break
    print(ans)
