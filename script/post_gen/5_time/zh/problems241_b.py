Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读入
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 处理
    A.sort()
    B.sort()
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] <= B[j]:
            i += 1
        j += 1
    # 输出
    if i == N:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def solution():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if max(A) < max(B):
        print('No')
    else:
        print('Yes')

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    a.sort()
    b.sort()

    i = 0
    j = 0

    while i < n and j < m:
        if a[i] <= b[j]:
            i += 1
        j += 1

    if i == n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    if n < m:
        print('No')
        return
    for i in range(m):
        if a[i] < b[i]:
            print('No')
            return
    print('Yes')

=======
Suggestion 5

def solve(n, m, a, b):
    if m > n:
        return False
    a.sort()
    b.sort()
    for i in range(m):
        if a[i] > b[i]:
            return False
    return True

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print('Yes' if solve(n, m, a, b) else 'No')

=======
Suggestion 6

def main():
    # n:面条的数量，m:需要的面条的数量
    n, m = map(int, input().split())
    # 面条的长度
    a = list(map(int, input().split()))
    # 需要的面条的长度
    b = list(map(int, input().split()))
    # 如果需要的面条的数量大于面条的数量，则不能完成计划
    if m > n:
        print('No')
        return
    # 面条的长度排序
    a.sort()
    # 需要的面条的长度排序
    b.sort()
    # 面条的长度
    a_index = 0
    # 需要的面条的长度
    b_index = 0
    # 需要的面条的数量
    b_count = 0
    # 遍历需要的面条的长度
    while b_index < m:
        # 如果需要的面条的长度小于面条的长度，则不能完成计划
        if b[b_index] < a[a_index]:
            print('No')
            return
        # 如果需要的面条的长度等于面条的长度，则需要的面条的数量加1
        if b[b_index] == a[a_index]:
            b_count += 1
            # 如果需要的面条的数量大于面条的数量，则不能完成计划
            if b_count > n:
                print('No')
                return
            # 如果需要的面条的数量等于面条的数量，则计划完成
            if b_count == n:
                print('Yes')
                return
            # 如果需要的面条的数量没有等于面条的数量，则面条的长度加1
            a_index += 1
        # 如果需要的面条的长度大于面条的长度，则面条的长度加1
        b_index += 1
    # 如果需要的面条的数量没有等于面条的数量，则不能完成计划
    if b_count != n:
        print('No')
        return

=======
Suggestion 7

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    if n<m:
        print("No")
    else:
        count = 0
        for i in range(m):
            for j in range(count,n):
                if A[j] == B[i]:
                    count += 1
                    break
        if count == m:
            print("Yes")
        else:
            print("No")
main()

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    if n < m:
        print('No')
        return
    a.sort(reverse=True)
    b.sort(reverse=True)

    i = 0
    j = 0
    while i < n and j < m:
        if a[i] >= b[j]:
            i += 1
            j += 1
        else:
            i += 1
    if j == m:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def get_input():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    return n, m, a, b

=======
Suggestion 10

def main():
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    if n < m:
        print("No")
    else:
        for i in range(m):
            if A[i] < B[i]:
                print("No")
                break
            else:
                if i == m-1:
                    print("Yes")
