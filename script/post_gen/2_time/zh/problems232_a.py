Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,m=map(int,input().split())
    a=[]
    b=[]
    for i in range(m):
        a1,b1=map(int,input().split())
        a.append(a1)
        b.append(b1)
    a.sort()
    b.sort()
    if a[0]==1 and b[m-1]==n:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    print(A)
    print(B)
    if N <= 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def problem231_d():
    pass

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    a = []
    b = []
    for i in range(m):
        a_i,b_i = map(int,input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    if a[m-1] < b[0]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    n,m = map(int,input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a = sorted(a)
    b = sorted(b)
    if a[m-1] > b[0]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A.sort()
    B.sort()
    if A[0] == 1 and B[-1] == N:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # 模拟
    # 人数为N，从1到N编号
    # 每次取出一个A_i,B_i，将其放在最左边或者最右边
    # 判断是否满足条件，不满足则返回No，满足则继续取下一个
    # 重复M次，若没有返回No，则返回Yes
    # 时间复杂度为O(MN)
    # 优化：使用集合存储每次的A_i,B_i，判断是否满足条件时，只需判断集合中是否存在A_i或B_i即可
    # 时间复杂度为O(M)
    # 优化：使用集合存储每次的A_i,B_i，判断是否满足条件时，只需判断集合中是否存在A_i或B_i即可
    # 时间复杂度为O(M)
    # 优化：使用集合存储每次的A_i,B_i，判断是否满足条件时，只需判断集合中是否存在A_i或B_i即可
    # 时间复杂度为O(M)
    # 优化：使用集合存储每次的A_i,B_i，判断是否满足条件时，只需判断集合中是否存在A_i或B_i即可
    # 时间复杂度为O(M)
    # 优化：使用集合存储每次的A_i,B_i，判断是否满足条件时，只需判断集合中是否存在A_i或B_i即可
    # 时间复杂度为O(M)
    # 优化：使用集合存储每次的A_i,B_i，判断是否满足条件时，只需判断集合中是否存在A_i

=======
Suggestion 8

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
Suggestion 9

def solve():
    n, m = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())

    # 1. b中的数字不能重复
    # 2. a中的数字不能重复
    # 3. a中的数字不能在b中出现
    # 4. a中的数字必须是1~n的连续数字
    # 5. b中的数字必须是1~n的连续数字
    # 6. a中的数字必须是b中数字的前一个或者后一个
    # 7. b中的数字必须是a中数字的前一个或者后一个
    # 8. a中的数字不能是b中数字的前一个或者后一个
    # 9. b中的数字不能是a中数字的前一个或者后一个
    # 10. a中的数字不能是b中数字的前一个或者后一个
    # 11. b中的数字不能是a中数字的前一个或者后一个
    # 12. a中的数字不能是b中数字的前一个或者后一个
    # 13. b中的数字不能是a中数字的前一个或者后一个
    # 14. a中的数字不能是b中数字的前一个或者后一个
    # 15. b中的数字不能是a中数字的前一个或者后一个
    # 16. a中的数字不能是b中数字的前一个或者后一个
    # 17. b中的数字不能是a中数字的前一个或者后一个
    # 18. a中的数字不能是b中数字的前一个或者后一个
    # 19. b中的数字不能是a中数字的前一个或者后一个
    # 20. a中的数字不能是b中数字的前一个或者后一个
    # 21. b中的数字不能是a中数字的前一个或者后一个
    # 22

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A.sort()
    B.sort()

    for i in range(M):
        if A[i] == 1:
            if B[i] == N:
                print("POSSIBLE")
                return
    print("IMPOSSIBLE")
