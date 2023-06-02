Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    print(N**2-len(A))

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    if M == 0:
        print(N)
        return
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    s = set()
    for i in range(M):
        for j in range(M):
            if A[i] == B[j]:
                s.add(A[i])
    print(N - len(s))
    return

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    AB = []
    for i in range(M):
        AB.append(list(map(int, input().split())))
    #print(N, M, AB)
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i != j:
                flag = True
                for k in range(M):
                    if i == AB[k][0] and j == AB[k][1]:
                        flag = False
                if flag:
                    count += 1
    print(count)
main()

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            cnt = 0
            for k in range(M):
                if A[k] == i+1 and B[k] == j+1:
                    cnt += 1
                if A[k] == j+1 and B[k] == i+1:
                    cnt += 1
            ans += cnt * (cnt-1) // 2

    print(ans)

=======
Suggestion 5

def get_input():
    n,m = map(int,input().split())
    ab = []
    for i in range(m):
        ab.append(list(map(int,input().split())))
    return n,m,ab

=======
Suggestion 6

def main():
    N,M = map(int,input().split())
    A = [0]*M
    B = [0]*M
    for i in range(M):
        A[i],B[i] = map(int,input().split())
    print(N*N-N-M)

=======
Suggestion 7

def get_input():
    n, m = map(int, input().split())
    ab = []
    for i in range(m):
        a, b = map(int, input().split())
        ab.append((a, b))
    return n, m, ab

=======
Suggestion 8

def problem204_c():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    A = set(A)
    B = set(B)
    print(N-len(A&B))
problem204_c()

=======
Suggestion 9

def f(n, m, l):
    ans = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                ans += l[i][j] * l[j][i]
    return ans

n, m = map(int, input().split())
l = [[0 for _ in range(n)] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    l[a-1][b-1] = 1
print(f(n, m, l))

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    # print(N, M, AB)
    # print(AB[0][0])

    # 1. 从1开始，遍历所有可能的路径
    # 2. 只要有一条路径能到达所有的点，就+1
    # 3. 用深度优先搜索，记录每个点的到达情况
    # 4. 如果某个点已经被访问过，就不再访问
    # 5. 如果某个点已经被访问过，就不再访问
    # 6. 如果某个点已经被访问过，就不再访问
    # 7. 重要的事情说三遍
    # 8. 用递归实现
    # 9. 用递归实现
    # 10. 用递归实现
    # 11. 用递归实现
    # 12. 用递归实现
    # 13. 用递归实现
    # 14. 用递归实现
    # 15. 用递归实现
    # 16. 用递归实现
    # 17. 用递归实现
    # 18. 用递归实现
    # 19. 用递归实现
    # 20. 用递归实现
    # 21. 用递归实现
    # 22. 用递归实现
    # 23. 用递归实现
    # 24. 用递归实现
    # 25. 用递归实现
    # 26. 用递归实现
    # 27. 用递归实现
    # 28. 用递
