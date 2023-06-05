Synthesizing 10/10 solutions

=======
Suggestion 1

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
                print(j + 1)
                break
        else:
            print(-1)

=======
Suggestion 2

def myfun(A, x, k):
    for i in range(0, len(A)):
        if A[i] == x:
            k -= 1
            if k == 0:
                return i + 1
    return -1

=======
Suggestion 3

def find_kth(a, x, k):
    cnt = 0
    for i in range(len(a)):
        if a[i] == x:
            cnt += 1
            if cnt == k:
                return i+1
    return -1

=======
Suggestion 4

def solution1():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for j in range(n):
            if a[j] == x:
                cnt += 1
                if cnt == k:
                    print(j+1)
                    break
        if cnt != k:
            print(-1)

=======
Suggestion 5

def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        x, k = map(int, input().split())
        cnt = 0
        for j in range(n):
            if x == a[j]:
                cnt += 1
            if cnt == k:
                print(j + 1)
                break
        else:
            print(-1)

solve()

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x_i, k_i = map(int, input().split())
        cnt = 0
        for j in range(N):
            if A[j] == x_i:
                cnt += 1
            if cnt == k_i:
                print(j+1)
                break
        else:
            print(-1)

=======
Suggestion 7

def main():
    N,Q = map(int,input().split())
    A = list(map(int,input().split()))
    for i in range(Q):
        x,k = map(int,input().split())
        print(A.index(x,k-1)+1 if x in A[k-1:] else -1)

=======
Suggestion 8

def main():
    n, q = input().split()
    n = int(n)
    q = int(q)
    a = input().split()
    for i in range(n):
        a[i] = int(a[i])
    for i in range(q):
        x, k = input().split()
        x = int(x)
        k = int(k)
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
Suggestion 9

def  binary_search(a, x, k):
    '''
    二分查找
    :param a: 数组
    :param x: 查找的数
    :param k: 第几次出现
    :return: 第k次出现的位置
    '''
    # print(a, x, k)
    if k == 1:
        for i in range(len(a)):
            if a[i] == x:
                return i
        return -1
    elif k == 2:
        for i in range(len(a)):
            if a[i] == x:
                k -= 1
            if k == 1:
                return i
        return -1
    else:
        if x in a:
            return a.index(x)
        else:
            return -1

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(Q):
        x, k = map(int, input().split())
        #print(x, k)
        count = 0
        for j in range(N):
            if A[j] == x:
                count += 1
                if count == k:
                    print(j+1)
                    break
        else:
            print(-1)
