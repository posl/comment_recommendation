def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i],B[i] = map(int,input().split())
    #print(A)
    #print(B)
    #print(N)
    #隣接リストを作成
    neighbor = [[] for _ in range(N)]
    for i in range(N-1):
        neighbor[A[i]-1].append(B[i]-1)
        neighbor[B[i]-1].append(A[i]-1)
    #print(neighbor)
    #深さ優先探索
    visited = [False] * N
    visited[0] = True
    stack = [0]
    ans = [0]
    while stack:
        #print(stack)
        #print(ans)
        node = stack.pop()
        for i in neighbor[node]:
            if visited[i] == False:
                visited[i] = True
                stack.append(node)
                stack.append(i)
                ans.append(i)
                break
        else:
            if node != 0:
                stack.append(neighbor[node][0])
                ans.append(neighbor[node][0])
    for i in range(N):
        print(ans[i]+1,end=" ")
