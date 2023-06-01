Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # 读取数据
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    # 读取查询
    query = []
    for i in range(q):
        x, k = map(int, input().split())
        query.append((x, k))

    # 处理查询
    for x, k in query:
        count = 0
        for i, num in enumerate(a):
            if num == x:
                count += 1
                if count == k:
                    print(i + 1)
                    break
        else:
            print(-1)

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        count = 0
        for j in range(n):
            if a[j] == x:
                count += 1
            if count == k:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    A = [int(_) for _ in input().split()]
    for _ in range(Q):
        x, k = map(int, input().split())
        count = 0
        for i in range(N):
            if A[i] == x:
                count += 1
                if count == k:
                    print(i+1)
                    break
        else:
            print(-1)

=======
Suggestion 4

def solve():
    n, q = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    for i in range(q):
        x, k = [int(x) for x in input().split()]
        cnt = 0
        for j in range(n):
            if a[j] == x:
                cnt += 1
            if cnt == k:
                print(j+1)
                break
        else:
            print(-1)

solve()

=======
Suggestion 5

def get_index(A, x, k):
    i = 0
    count = 0
    for a in A:
        if a == x:
            count += 1
            if count == k:
                return i + 1
        i += 1
    return -1

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        count = 0
        for j in range(N):
            if A[j] == x:
                count += 1
            if count == k:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 7

def main():
    # 读取输入
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    # 处理查询
    for i in range(q):
        x, k = map(int, input().split())
        # 从第一个元素开始计数
        count = 0
        # 记录当前元素的下标
        index = 0
        # 从第一个元素开始遍历
        for j in range(n):
            # 如果当前元素等于x，则计数加1
            if a[j] == x:
                count += 1
                # 如果计数等于k，则打印当前元素的下标，然后跳出循环
                if count == k:
                    print(j + 1)
                    break
                # 否则，更新当前元素的下标，继续遍历
                else:
                    index = j
        # 如果遍历结束后，计数还是小于k，则打印-1
        if count < k:
            print(-1)

=======
Suggestion 8

def get_answer(a, x, k):
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
            if count == k:
                return i+1
    return -1

=======
Suggestion 9

def solve(n, q, a, x, k):
    # 用于存储每个数字的索引
    d = {}
    for i in range(n):
        if a[i] not in d:
            d[a[i]] = []
        d[a[i]].append(i + 1)
    # print(d)
    for i in range(q):
        if x[i] not in d:
            print(-1)
        elif len(d[x[i]]) < k[i]:
            print(-1)
        else:
            print(d[x[i]][k[i] - 1])
