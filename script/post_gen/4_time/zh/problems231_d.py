Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    N, M = map(int, input().split())
    A, B = [], []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 计算每个人的入度
    in_degrees = [0] * (N + 1)
    for i in range(M):
        in_degrees[B[i]] += 1

    # 计算拓扑排序的结果
    result = []
    queue = []
    for i in range(1, N + 1):
        if in_degrees[i] == 0:
            queue.append(i)
    while len(queue) > 0:
        v = queue.pop(0)
        result.append(v)
        for i in range(M):
            if A[i] == v:
                in_degrees[B[i]] -= 1
                if in_degrees[B[i]] == 0:
                    queue.append(B[i])

    # 检查是否有环
    if len(result) != N:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a1,b1 = map(int,input().split())
        a.append(a1)
        b.append(b1)
    a.sort()
    b.sort()
    if a[0] == 1 and b[-1] == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def check(n,m,ai,bi):
    #print(n,m,ai,bi)
    if n == 1:
        print("Yes")
        return
    if m == 0:
        print("No")
        return
    if m == 1:
        print("Yes")
        return
    if m == 2:
        if ai[0] == 1 or ai[1] == 1 or bi[0] == n or bi[1] == n:
            print("Yes")
        else:
            print("No")
        return
    if m == 3:
        if ai[0] == 1 or ai[1] == 1 or ai[2] == 1 or bi[0] == n or bi[1] == n or bi[2] == n:
            print("Yes")
        else:
            print("No")
        return
    print("Yes")
    return
n,m = map(int,input().split())
ai = []
bi = []
for i in range(m):
    a,b = map(int,input().split())
    ai.append(a)
    bi.append(b)
check(n,m,ai,bi)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # print(A)
    # print(B)
    # print(N)
    # print(M)

    # 1. 建立邻接表
    # 2. 深度优先搜索
    # 3. 从一个节点开始，遍历所有节点，如果有一个节点没有被遍历到，则返回False
    # 4. 如果所有节点都被遍历到了，则返回True
    # 5. 从一个节点开始，遍历所有节点，如果有一个节点没有被遍历到，则返回False
    # 6. 如果所有节点都被遍历到了，则返回True
    # 7. 从一个节点开始，遍历所有节点，如果有一个节点没有被遍历到，则返回False
    # 8. 如果所有节点都被遍历到了，则返回True
    # 9. 从一个节点开始，遍历所有节点，如果有一个节点没有被遍历到，则返回False
    # 10. 如果所有节点都被遍历到了，则返回True
    # 11. 从一个节点开始，遍历所有节点，如果有一个节点没有被遍历到，则返回False
    # 12. 如果所有节点都被遍历到了，则返回True
    # 13. 从一个节点开始，遍历所有节点，如果有一个节点没有被遍历到，则返回False
    # 14. 如果所有节点都被遍历到了，则返回True
    # 15. 从一个节点开始，遍历所有节点，如果有一个节点没有被遍历到，则返回False
    # 16. 如果所有节点都被遍历到了，则返回True
    # 17. 从一个节点开始，遍历所有节点，如果有一个节点没有被遍历到，则返回False
    #

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    print(A)
    print(B)
    print(N)
    print(M)
    return

main()

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    a = [0] * N
    for i in range(M):
        A, B = map(int, input().split())
        a[A - 1] += 1
        a[B - 1] += 1
    for i in range(N):
        if a[i] % 2 == 1:
            print("No")
            return
    print("Yes")
solve()

=======
Suggestion 7

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[M-1] < B[0]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def check(a, b):
    if a == b:
        return False
    if a > b:
        a, b = b, a
    if a == 1 and b == N:
        return False
    if b - a == 1:
        return False
    return True


N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

=======
Suggestion 9

def dfs(i):
    visited[i] = 1
    for j in G[i]:
        if visited[j] == 1:
            return False
        elif visited[j] == 0:
            if not dfs(j):
                return False
    visited[i] = 2
    return True

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
visited = [0] * N
for i in range(N):
    if visited[i] == 0:
        if not dfs(i):
            print("No")
            exit()
print("Yes")

=======
Suggestion 10

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    print(A)
    print(B)
    A.sort()
    B.sort()
    print(A)
    print(B)
    if A[-1] < B[0]:
        print('Yes')
    else:
        print('No')
