Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def solve(arr):
    return arr

=======
Suggestion 3

def main():
    n = int(input())
    A = []
    for i in range(n):
        query = input().split()
        if query[0] == "1":
            A.append(int(query[1]))
        elif query[0] == "2":
            x = int(query[1])
            k = int(query[2])
            count = 0
            for a in A:
                if x >= a:
                    count += 1
            if count >= k:
                print(sorted(A, reverse=True)[k-1])
            else:
                print("-1")
        elif query[0] == "3":
            x = int(query[1])
            k = int(query[2])
            count = 0
            for a in A:
                if x <= a:
                    count += 1
            if count >= k:
                print(sorted(A)[k-1])
            else:
                print("-1")

=======
Suggestion 4

def main():
    # 读取输入
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(input().split())
    #print(queries)
    # 处理输入
    a = []
    for query in queries:
        if query[0] == '1':
            a.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i <= x]
            b.sort(reverse=True)
            if len(b) >= k:
                print(b[k-1])
            else:
                print(-1)
        else:
            x = int(query[1])
            k = int(query[2])
            b = [i for i in a if i >= x]
            b.sort()
            if len(b) >= k:
                print(b[k-1])
            else:
                print(-1)
    return

=======
Suggestion 5

def main():
    # 问题陈述
    # 我们有一个空序列A。
    # 给出Q个查询，按顺序处理它们。
    # 每个查询都是以下三种类型中的一种。
    # 1 x : 向A插入x。
    # 2 x k : 在A中小于或等于x的元素中，打印第k个最大值。  (k不超过5)
    # 如果A中小于等于或等于x的元素少于k，则打印-1。
    # 3 x k : 在A中大于或等于x的元素中，打印第k个最小的值。  (k不超过5)
    # 如果A中小于k的元素大于或等于x，则打印-1。
    #
    #
    # 限制条件
    # 1≦ Q ≦ 2× 10^5
    # 1≦ x≦ 10^{18}
    # 1≦ k≦ 5
    # 输入的所有数值都是整数。
    #
    # 输入
    # 输入是由标准输入提供的，格式如下：
    # Q
    # query_1
    # query_2
    # .
    # .
    # .
    # query_Q
    # 在第i个查询query_i中，首先给出查询的类型c_i（是1，2，还是3）。
    # 如果c_i=1，则另外给出x；如果c_i=2，3，则另外给出x和k。
    # 换句话说，每个查询都是以以下三种格式之一给出的：
    # 1 x
    # 2 x k
    # 3 x k
    #
    # 输出
    # 打印q行，其中q是指c_i=2,3的查询的数量。
    # 第j行（1≦ j≦ q）应该包含第j个这样的查询的答案。
    #
    # 输入样本 1

=======
Suggestion 6

def main():
    from bisect import bisect_left, bisect_right
    from collections import defaultdict
    from sys import stdin
    input = stdin.readline

    q = int(input())
    a = []
    d = defaultdict(list)
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            a.append(query[1])
            d[query[1]].append(len(a) - 1)
        elif query[0] == 2:
            if len(a) == 0:
                print(-1)
            else:
                i = bisect_right(a, query[1])
                if i == 0:
                    print(-1)
                else:
                    print(a[d[a[i - 1]][query[2] - 1]])
        else:
            if len(a) == 0:
                print(-1)
            else:
                i = bisect_left(a, query[1])
                if i == len(a):
                    print(-1)
                else:
                    print(a[d[a[i]][query[2] - 1]])

=======
Suggestion 7

def main():
    n = int(input())
    a = []
    for i in range(n):
        s = input().split()
        if s[0] == "1":
            a.append(int(s[1]))
        elif s[0] == "2":
            a.sort()
            if len(a) < int(s[2]):
                print(-1)
            else:
                print(a[-int(s[2])])
        elif s[0] == "3":
            a.sort()
            if len(a) < int(s[2]):
                print(-1)
            else:
                print(a[int(s[2])-1])

=======
Suggestion 8

def main():
    n = int(input())
    for i in range(n):
        a = list(map(int, input().split()))
        if a[0] == 1:
            A.append(a[1])
        elif a[0] == 2:
            print(max(sorted(A)[:a[2]]))
        else:
            print(min(sorted(A)[::-1][:a[2]]))

A = []
main()

=======
Suggestion 9

def main():
    n = int(input())
    A = []
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            B = []
            for a in A:
                if a <= x:
                    B.append(a)
            B.sort(reverse=True)
            if len(B) < k:
                print(-1)
            else:
                print(B[k-1])
        elif query[0] == '3':
            x = int(query[1])
            k = int(query[2])
            B = []
            for a in A:
                if a >= x:
                    B.append(a)
            B.sort()
            if len(B) < k:
                print(-1)
            else:
                print(B[k-1])

=======
Suggestion 10

def insert(x):
    global n
    n += 1
    a[n] = x
    i = n
    while i > 1:
        if a[i] < a[i // 2]:
            a[i], a[i // 2] = a[i // 2], a[i]
            i //= 2
        else:
            break
