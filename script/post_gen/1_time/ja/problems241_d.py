Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            B = [x for x in A if x <= query[1]]
            B.sort(reverse=True)
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[query[2]-1])
        elif query[0] == 3:
            B = [x for x in A if x >= query[1]]
            B.sort()
            if len(B) < query[2]:
                print(-1)
            else:
                print(B[query[2]-1])
        else:
            print("error")
            break

=======
Suggestion 2

def main():
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            if query[1] <= A[0]:
                print(-1)
            else:
                if len(A) < query[2]:
                    print(-1)
                else:
                    print(A[query[2]-1])
        else:
            A.sort(reverse=True)
            if query[1] >= A[0]:
                print(-1)
            else:
                if len(A) < query[2]:
                    print(-1)
                else:
                    print(A[query[2]-1])

=======
Suggestion 3

def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            if len(A) < query[2]:
                print(-1)
            else:
                A.sort(reverse=True)
                print(A[query[2] - 1])
        elif query[0] == 3:
            if len(A) < query[2]:
                print(-1)
            else:
                A.sort()
                print(A[query[2] - 1])

=======
Suggestion 4

def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            ans = 0
            for i in range(len(A)):
                if A[i] > query[1]:
                    ans = A[i-1]
                    break
            if ans == 0:
                ans = A[-1]
            print(ans)
        elif query[0] == 3:
            A.sort()
            ans = 0
            for i in range(len(A)):
                if A[i] >= query[1]:
                    ans = A[i]
                    break
            if ans == 0:
                ans = -1
            print(ans)

=======
Suggestion 5

def main():
    Q = int(input())
    A = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        else:
            x,k = query[1],query[2]
            if query[0] == 2:
                A.sort(reverse=True)
                ans = -1
                count = 0
                for i in A:
                    if i <= x:
                        count += 1
                        if count == k:
                            ans = i
                            break
            else:
                A.sort()
                ans = -1
                count = 0
                for i in A:
                    if i >= x:
                        count += 1
                        if count == k:
                            ans = i
                            break
            if ans != -1:
                print(ans)

=======
Suggestion 6

def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    A = []
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            if query[1] >= A[-1]:
                print(-1)
            else:
                for i in range(len(A)):
                    if A[i] > query[1]:
                        if len(A[i:]) >= query[2]:
                            print(A[i+query[2]-1])
                        else:
                            print(-1)
                        break
        else:
            A.sort(reverse=True)
            if query[1] <= A[-1]:
                print(-1)
            else:
                for i in range(len(A)):
                    if A[i] < query[1]:
                        if len(A[i:]) >= query[2]:
                            print(A[i+query[2]-1])
                        else:
                            print(-1)
                        break

=======
Suggestion 7

def main():
    from bisect import bisect_left, bisect_right
    q = int(input())
    a = []
    for _ in range(q):
        c, *x = map(int, input().split())
        if c == 1:
            a.append(x[0])
        else:
            x, k = x
            if c == 2:
                i = bisect_left(a, x)
                if i + k - 1 < len(a):
                    print(a[i + k - 1])
                else:
                    print(-1)
            else:
                i = bisect_right(a, x)
                if i - k >= 0:
                    print(a[i - k])
                else:
                    print(-1)

=======
Suggestion 8

def main():
    #入力
    Q = int(input())
    A = []
    for q in range(Q):
        query = list(map(int,input().split()))
        if query[0] == 1:
            A.append(query[1])
        elif query[0] == 2:
            A.sort()
            A = list(set(A))
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[query[2]-1])
        elif query[0] == 3:
            A.sort(reverse=True)
            A = list(set(A))
            if len(A) < query[2]:
                print(-1)
            else:
                print(A[query[2]-1])

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline

    #入力
    Q = int(input())
    query = [list(map(int, input().split())) for _ in range(Q)]

    #処理
    A = []
    for i in range(Q):
        if query[i][0] == 1:
            A.append(query[i][1])
        elif query[i][0] == 2:
            A.sort(reverse=True)
            for j in range(len(A)):
                if A[j] <= query[i][1]:
                    if j+1 == query[i][2]:
                        print(A[j])
                    elif j+1 > query[i][2]:
                        print(-1)
                    break
        elif query[i][0] == 3:
            A.sort()
            for j in range(len(A)):
                if A[j] >= query[i][1]:
                    if j+1 == query[i][2]:
                        print(A[j])
                    elif j+1 > query[i][2]:
                        print(-1)
                    break

=======
Suggestion 10

def main():
    import sys
    from bisect import bisect_left, bisect_right
    from collections import defaultdict
    input = sys.stdin.readline
    Q = int(input())
    A = []
    d = defaultdict(list)
    ans = []
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            d[x].append(len(A))
            A.append(x)
        elif query[0] == 2:
            x = query[1]
            k = query[2]
            if k > len(d[x]):
                ans.append(-1)
            else:
                ans.append(A[d[x][k-1]])
        elif query[0] == 3:
            x = query[1]
            k = query[2]
            if k > len(A) - bisect_right(A, x):
                ans.append(-1)
            else:
                ans.append(A[bisect_right(A, x)+k-1])
    print(*ans, sep='
')
main()
