Synthesizing 10/10 solutions

=======
Suggestion 1

def search(a, x, k):
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
            if count == k:
                return i + 1
    return -1

=======
Suggestion 2

def solution():
    pass

=======
Suggestion 3

def find(x, k):
    cnt = 0
    for i in range(len(A)):
        if A[i] == x:
            cnt += 1
            if cnt == k:
                return i + 1
    return -1

N, Q = map(int, input().split())
A = list(map(int, input().split()))
X = []
K = []
for i in range(Q):
    x, k = map(int, input().split())
    X.append(x)
    K.append(k)

for i in range(Q):
    print(find(X[i], K[i]))

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    n,q = map(int,input().split())
    a = list(map(int,input().split()))
    print(a)
    for i in range(q):
        x,k = map(int,input().split())
        print("x:%d k:%d"%(x,k))
        if k > a.count(x):
            print(-1)
        else:
            count = 0
            for j in range(len(a)):
                if a[j] == x:
                    count += 1
                    if count == k:
                        print(j+1)
                        break

=======
Suggestion 6

def read_int():
    return int(input())

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    for _ in range(q):
        x, k = map(int, input().split())
        count = 0
        for i, v in enumerate(a):
            if v == x:
                count += 1
            if count == k:
                print(i + 1)
                break
        else:
            print(-1)

=======
Suggestion 8

def search(x,k):
    index = 0
    for i in range(k):
        index = A.index(x,index)
        if index == -1:
            return -1
        index += 1
    return index

N,Q = input().split()
N = int(N)
Q = int(Q)
A = input().split()
A = [int(i) for i in A]
for i in range(Q):
    x,k = input().split()
    x = int(x)
    k = int(k)
    print(search(x,k))

=======
Suggestion 9

def findKthElement(a, x, k):
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
            if count == k:
                return i+1
    return -1

=======
Suggestion 10

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
