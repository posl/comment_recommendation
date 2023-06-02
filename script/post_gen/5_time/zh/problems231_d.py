Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    # 1...N
    # 1...M
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    # print(A, B)
    # 1...N
    # 1...M
    # A[i] - 1, B[i] - 1
    # A[i] - 1, B[i] - 1
    # A[i] - 1, B[i] - 1
    # 1...N
    # 1...M
    # A[i] - 1, B[i] - 1
    # A[i] - 1, B[i] - 1
    # A[

=======
Suggestion 2

def solve():
    N,M = map(int,input().split())
    A = []
    B = []
    for i in range(M):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A,B)
    #print(N,M)
    #print(N-1)
    #print(A.count(1))
    if N == 1:
        print("Yes")
        return
    if N-1 == A.count(1):
        print("Yes")
        return
    print("No")
    return

=======
Suggestion 3

def solve(n, m, a, b):
    # 从1开始，每个人的左右邻居
    neighbors = [set() for _ in range(n + 1)]
    for i in range(m):
        neighbors[a[i]].add(b[i])
        neighbors[b[i]].add(a[i])

    # 从1开始，每个人的左右邻居的左右邻居
    neighbors2 = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in neighbors[i]:
            for k in neighbors[j]:
                if k != i:
                    neighbors2[i].add(k)

    # 从1开始，每个人的左右邻居的左右邻居的左右邻居
    neighbors3 = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in neighbors2[i]:
            for k in neighbors[j]:
                if k != i and k not in neighbors[i]:
                    neighbors3[i].add(k)

    # 从1开始，每个人的左右邻居的左右邻居的左右邻居的左右邻居
    neighbors4 = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in neighbors3[i]:
            for k in neighbors[j]:
                if k != i and k not in neighbors[i] and k not in neighbors2[i]:
                    neighbors4[i].add(k)

    # 从1开始，每个人的左右邻居的左右邻居的左右邻居的左右邻居的左右邻居
    neighbors5 = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in neighbors4[i]:
            for k in neighbors[j]:
                if k != i and k not in neighbors[i] and k not in neighbors2[i] and k not in neighbors3[i]:
                    neighbors5[i].add(k)

    # 从1开始，每个人的左右邻居的

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    if m == 0:
        print('No')
    else:
        a = []
        b = []
        for i in range(m):
            a1,b1 = map(int,input().split())
            a.append(a1)
            b.append(b1)
        a.sort()
        b.sort()
        if b[0] - a[-1] == 1:
            print('No')
        else:
            print('Yes')

=======
Suggestion 5

def main():
    n,m=map(int,input().split())
    a=[0]*n
    b=[0]*n
    for i in range(m):
        a[i],b[i]=map(int,input().split())
    for i in range(m):
        a[i]-=1
        b[i]-=1
    a.sort()
    b.sort()
    for i in range(m-1):
        if b[i]==a[i+1]:
            print("No")
            return
    print("Yes")

=======
Suggestion 6

def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    # 1. 判断是否有办法让人们排队满足条件
    # 2. 打印Yes；如果没有，则打印No。
    # 3. 满足所有条件的一种方法是将它们按4,1,3,2的顺序排列。
    # 4. 没有办法将它们排成一排以满足所有的条件。
    # 5. 1 <= A_i < B_i <= N
    # 6. 2 <= N <= 10^5
    # 7. 0 <= M <= 10^5
    # 8. 所有的对（A_i,B_i）都是不同的。

    # 1. 判断是否有办法让人们排队满足条件
    # 2. 打印Yes；如果没有，则打印No。
    # 3. 满足所有条件的一种方法是将它们按4,1,3,2的顺序排列。
    # 4. 没有办法将它们排成一排以满足所有的条件。
    # 5. 1 <= A_i < B_i <= N
    # 6. 2 <= N <= 10^5
    # 7. 0 <= M <= 10^5
    # 8. 所有的对（A_i,B_i）都是不同的。
    # 9. 1 <= A_i < B_i <= N
    # 10. 2 <= N <= 10^5
    # 11. 0 <= M <= 10^5
    # 12. 所有的对（A_i,B_i）都是不同的。
    # 13. 1 <= A_i < B_i <= N
    # 14. 2 <= N <= 10

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    for i in range(M):
        if A[i] > B[i]:
            A[i], B[i] = B[i], A[i]
    for i in range(M - 1):
        if B[i] != A[i + 1]:
            print("No")
            return
    print("Yes")
    return

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
    #print(A)
    #print(B)
    #print(N)
    #print(M)
    #print(len(A))
    #print(len(B))
    for i in range(M):
        if A[i] == 1:
            for j in range(M):
                if B[i] == A[j]:
                    if B[j] == N:
                        print("Yes")
                        return
    print("No")
    return

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    f = [0] * (N + 2)
    for i in range(M):
        a, b = map(int, input().split())
        f[a] += 1
        f[b + 1] -= 1
    for i in range(1, N + 1):
        f[i] += f[i - 1]
    for i in range(1, N + 1):
        if f[i] == 0:
            print("No")
            return
    print("Yes")
    return

=======
Suggestion 10

def main():
    # 读取输入
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    # 从1开始，每个人的编号
    people = [i for i in range(1, N + 1)]
    # 人的编号和索引的对应关系
    people_dict = {i: i - 1 for i in people}
    # 人的索引和编号的对应关系
    people_dict_reverse = {i - 1: i for i in people}
    # 人的左右关系
    left_right_dict = {i: [i - 1, i + 1] for i in people}
    # 人的左右关系，去除边界的人
    left_right_dict[1] = [2]
    left_right_dict[N] = [N - 1]
    # 人的左右关系，去除边界的人
    for i in range(2, N):
        left_right_dict[i] = [i - 1, i + 1]
    # print(people)
    # print(people_dict)
    # print(people_dict_reverse)
    # print(left_right_dict)
    # 按照条件，依次交换位置
    for i in range(M):
        # print("第{}次交换".format(i))
        a = A[i]
        b = B[i]
        # print("交换前：", people)
        # print("交换前：", left_right_dict)
        # print("交换前：", people_dict)
        # print("交换前：", people_dict_reverse)
        # 交换位置
        # 交换人的编号
        people_dict[a], people_dict[b] = people_dict[b], people_dict[a]
        # 交换人的索引
        people_dict_reverse[people_dict[a]], people_dict_reverse[people_dict[b]] = people_dict_reverse[people_dict[b]], people_dict_reverse[people_dict[a]]
        # 交换人的左右关系
        left_right_dict[people_dict[a]], left_right_dict
