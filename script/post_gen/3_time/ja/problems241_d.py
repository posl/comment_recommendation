Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            B = [x for x in A if x <= query[1]]
            B.sort(reverse=True)
            if len(B) >= query[2]:
                print(B[query[2]-1])
            else:
                print(-1)
        elif query[0] == 3:
            A.sort()
            B = [x for x in A if x >= query[1]]
            B.sort()
            if len(B) >= query[2]:
                print(B[query[2]-1])
            else:
                print(-1)
        else:
            print("error")
            break

=======
Suggestion 2

def main():
    N = int(input())
    A = []
    for i in range(N):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A = sorted(A)
            B = []
            for j in range(len(A)):
                if A[j] <= query[1]:
                    B.append(A[j])
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[-query[2]])
        else:
            A = sorted(A, reverse=True)
            B = []
            for j in range(len(A)):
                if A[j] >= query[1]:
                    B.append(A[j])
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[-query[2]])

=======
Suggestion 3

def main():
    q = int(input())
    a = []
    for i in range(q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            a.append(query[1])
        elif query[0] == 2:
            a.sort()
            a = list(reversed(a))
            if len(a) >= query[2]:
                print(a[query[2]-1])
            else:
                print(-1)
        else:
            a.sort()
            if len(a) >= query[2]:
                print(a[query[2]-1])
            else:
                print(-1)

=======
Suggestion 4

def main():
    N = int(input())
    A = []
    for i in range(N):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            A = list(reversed(A))
            if len(A) >= query[2]:
                print(A[query[2]-1])
            else:
                print("-1")
        elif query[0] == 3:
            A.sort()
            if len(A) >= query[2]:
                print(A[query[2]-1])
            else:
                print("-1")
        else:
            print("Error")
            break

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    for i in range(N):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            B = sorted([a for a in A if a <= query[1]])
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[-query[2]])
        elif query[0] == 3:
            B = sorted([a for a in A if a >= query[1]])
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[query[2]-1])

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    A = []
    ans = []
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        else:
            x = query[1]
            k = query[2]
            B = [a for a in A if a <= x]
            B.sort(reverse=True)
            if len(B) < k:
                ans.append(-1)
            else:
                ans.append(B[k-1])
    print(*ans, sep='

')

=======
Suggestion 7

def main():
    import sys
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines
    N, *A = map(int, rea

=======
Suggestion 8

def main():
    import sys
    input = sys.stdin.readline
    from bisect import bisect_left, bisect_right
    Q = int(input())
    A = []
    ans = []
    for i in range(Q):
        c, *x = map(int, input().split())
        if c == 1:
            A.append(x[0])
        elif c == 2:
            a = bisect_left(A, x[0])
            if len(A) - a < x[1]:
                ans.append(-1)
            else:
                ans.append(A[a+x[1]-1])
        else:
            a = bisect_right(A, x[0])
            if a < x[1]:
                ans.append(-1)
            else:
                ans.append(A[a-x[1]])
    for i in ans:
        print(i)

=======
Suggestion 9

def main():
    import sys
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    A = []
    D = defaultdict(int)
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
            D[query[1]] += 1
        elif query[0] == 2:
            A.sort()
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[query[2]-1])
        else:
            A.sort(reverse = True)
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[query[2]-1])

=======
Suggestion 10

def main():
    # 入力
    Q = int(input())
    query = []
    for i in range(Q):
        query.append(list(map(int,input().split())))
    # 処理
    # A = []
    A = [0] * Q
    # A = [0] * 10**5
    # A = [0] * 2*10**5
    # A = [0] * 10**18
    # A = [0] * 2*10**18
    # A = [0] * 10**20
    # A = [0] * 2*10**20
    # A = [0] * 10**25
    # A = [0] * 2*10**25
    
    # A = [0] * 10**18
    # A = [0] * 10**20
    # A = [0] * 10**30
    # A = [0] * 10**50
    # A = [0] * 10**100
    # A = [0] * 10**1000
    # A = [0] * 10**10000
    # A = [0] * 10**100000
    # A = [0] * 10**1000000
    # A = [0] * 10**10000000
    # A = [0] * 10**100000000
    # A = [0] * 10**1000000000
    # A = [0] * 10**10000000000
    # A = [0] * 10**100000000000
    # A = [0] * 10**1000000000000
    # A = [0] * 10**10000000000000
    # A = [0] * 10**100000000000000
    # A = [0] * 10**1000000000000000
    # A = [0] * 10**10000000000000000
    # A = [0] * 10**100000000000000000
    # A = [0] * 10**1000000000000000000
    # A = [0] *
