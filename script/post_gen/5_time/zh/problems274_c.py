Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = [int(x) for x in

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * (2*N+1)
    for i in range(N):
        ans[A[i]] = i+1
    for i in range(1, 2*N):
        if ans[i] == 0:
            ans[i] = ans[i//2] + 1
    print('\n'.join(map(str, ans[1:])))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0]*(2*n+1)
    for i in range(n):
        b[a[i]] = i+1
    for i in range(1, 2*n+1):
        j = i
        print(0)
        while j != 1:
            j //= 2
            print(i-b[j])

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * (2 * N + 1)
    for i in range(N):
        B[A[i]] = i + 1
    for i in range(1, 2 * N):
        B[i + 1] = max(B[i + 1], B[i])
    for i in range(1, 2 * N + 1):
        print(B[i] - 1)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)

    #result = [0]*(2*N+1)
    #print(result)

    #for i in range(2*N+1):
    #    print(i)

    #for i in range(2*N+1):
    #    print(A[i])

    #for i in range(2*N+1):
    #    print(result[i])

    #print('--------------------------')

    result = [0]*(2*N+1)
    #print(result)

    for i in range(N):
        #print(i)
        #print(A[i])
        result[A[i]] = 1
        #print(result)
        #print(result[2*i])
        #print(result[2*i+1])
        result[2*i] = result[A[i]] + 1
        result[2*i+1] = result[A[i]] + 1
        #print(result)
        #print(result[2*i])
        #print(result[2*i+1])
        #print('--------------------------')

    for i in range(1, 2*N+1):
        print(result[i])

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = [0] * (2 * N + 1)
    for i in range(N):
        result[A[i]] = i + 1
    for i in range(1, N + 1):
        k = i
        while k != 1:
            k = k // 2
            result[k] = max(result[2 * k], result[2 * k + 1]) + 1
    for i in range(1, 2 * N + 1):
        print(result[i])

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.insert(0, 0)

    # 1. 二叉树的层次遍历
    # 2. 求二叉树每层的节点数
    # 3. 求二叉树每层的最大值
    # 4. 求二叉树每层的最小值
    # 5. 求二叉树的最大深度
    # 6. 求二叉树的最小深度
    # 7. 求二叉树的节点数
    # 8. 求二叉树的叶子节点数
    # 9. 求二叉树的第k层的节点数
    # 10. 求二叉树中两个节点的最低公共祖先节点
    # 11. 求二叉树中节点的最大距离
    # 12. 求二叉树中节点的最大距离，该节点可以不经过根节点
    # 13. 求二叉树中节点的最大距离，该节点只能是根节点或者是叶子节点
    # 14. 求二叉树中节点的最大距离，该节点只能是叶子节点
    # 15. 求二叉树中叶子节点的最大距离
    # 16. 求二叉树中两个节点之间的最大距离
    # 17. 求二叉树的镜像
    # 18. 求二叉树中两个节点的最低公共祖先节点
    # 19. 求二叉树中节点的最大距离，该节点可以不经过根节点
    # 20

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * (2*n+1)
    for i in range(n):
        ans[a[i]] = i+1
    for i in range(2*n-1, 0, -1):
        ans[i] = max(ans[2*i], ans[2*i+1]) + 1
    for i in range(1, 2*n+1):
        print(ans[i])

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = [0 for i in range(2*N+1)]
    for i in range(N):
        result[A[i]] = 1
    for i in range(2*N+1):
        if result[i] == 1:
            print(0)
        else:
            print(get_distance(i, result))

=======
Suggestion 10

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    res = [0] * (2 * n + 1)
    res[1] = 0
    for i in range(n):
        res[2 * i + 2] = res[A[i]] + 1
        res[2 * i + 3] = res[A[i]] + 1
    for i in range(1, 2 * n + 1):
        print(res[i])
