Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = []
    for i in range(Q):
        BC.append(list(map(int, input().split())))
    #print(N, A, Q, BC)
    sum_A = sum(A)
    #print(sum_A)
    for i in range(Q):
        sum_A += (BC[i][1] - BC[i][0]) * A.count(BC[i][0])
        print(sum_A)
        A = [BC[i][1] if x == BC[i][0] else x for x in A]
        #print(A)
    return

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for _ in range(Q)]

    sum = 0
    for a in A:
        sum += a

    for bc in BC:
        b = bc[0]
        c = bc[1]
        sum += (c - b) * A.count(b)
        print(sum)
        for i in range(len(A)):
            if A[i] == b:
                A[i] = c

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]

    sum = 0
    for i in range(N):
        sum += A[i]

    for i in range(Q):
        sum += (BC[i][1] - BC[i][0]) * A.count(BC[i][0])
        print(sum)
        sum = sum - (BC[i][1] - BC[i][0]) * A.count(BC[i][0])

        A = [BC[i][1] if x == BC[i][0] else x for x in A]

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]

    # print(a)
    # print(bc)

    s = sum(a)

    for b, c in bc:
        s += (c - b) * a.count(b)
        print(s)
        a = [c if x == b else x for x in a]

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    BC = [list(map(int,input().split())) for _ in range(Q)]
    sum_A = sum(A)
    BC = sorted(BC,key = lambda x:x[1],reverse = True)
    for i in range(Q):
        sum_A = sum_A - A[BC[i][0]-1] * (BC[i][1]-BC[i][0])
        A[BC[i][0]-1] = BC[i][1]
        print(sum_A)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]
    
    sum_a = sum(a)
    cnt = [0] * 100001
    for i in a:
        cnt[i] += 1
    
    for b, c in bc:
        sum_a -= cnt[b] * b
        sum_a += cnt[b] * c
        cnt[c] += cnt[b]
        cnt[b] = 0
        print(sum_a)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    bc = [list(map(int, input().split())) for _ in range(q)]

    sum_a = sum(a)
    dic = {i:0 for i in range(1, 10**5+1)}
    for i in a:
        dic[i] += 1

    for b, c in bc:
        sum_a += (c-b)*dic[b]
        dic[c] += dic[b]
        dic[b] = 0
        print(sum_a)

=======
Suggestion 8

def input_data():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    b = []
    c = []
    for i in range(q):
        b1, c1 = map(int, input().split())
        b.append(b1)
        c.append(c1)
    return n, a, q, b, c

=======
Suggestion 9

def get_sum(A):
    sum = 0
    for i in A:
        sum += i
    return sum

=======
Suggestion 10

def main():
    # 读取输入
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    BC = [input().split() for i in range(Q)]
    # 处理
    # 用字典保存每个数出现的次数
    d = dict()
    for i in A:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    # 计算初始和
    sum = 0
    for i in d:
        sum += i * d[i]
    # 每次操作
    for i in range(Q):
        b = int(BC[i][0])
        c = int(BC[i][1])
        # 更新字典
        if b in d:
            d[c] = d[c] + d[b]
            sum += (c - b) * d[b]
            del d[b]
        # 输出
        print(sum)
