Synthesizing 10/10 solutions

=======
Suggestion 1

def insert(A, x):
    A.append(x)
    A.sort()

=======
Suggestion 2

def insert(a,x):
    i = 0
    while i < len(a):
        if x <= a[i]:
            break
        i += 1
    a.insert(i,x)

=======
Suggestion 3

def main():
    n = int(input())
    for i in range(n):
        query = input().split()
        if query[0] == '1':
            A.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            B = [y for y in A if y <= x]
            B.sort(reverse=True)
            if len(B) < k:
                print(-1)
            else:
                print(B[k-1])
        elif query[0] == '3':
            x = int(query[1])
            k = int(query[2])
            B = [y for y in A if y >= x]
            B.sort()
            if len(B) < k:
                print(-1)
            else:
                print(B[k-1])
        else:
            print('error')

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    for i in range(n):
        s = input().split()
        if s[0] == "1":
            a.append(int(s[1]))
        elif s[0] == "2":
            x = int(s[1])
            k = int(s[2])
            b = []
            for j in a:
                if j <= x:
                    b.append(j)
            if len(b) < k:
                print(-1)
            else:
                b.sort(reverse=True)
                print(b[k-1])
        else:
            x = int(s[1])
            k = int(s[2])
            b = []
            for j in a:
                if j >= x:
                    b.append(j)
            if len(b) < k:
                print(-1)
            else:
                b.sort()
                print(b[k-1])

=======
Suggestion 5

def main():
    import sys
    from bisect import bisect_left, bisect_right
    input = sys.stdin.readline
    Q = int(input())
    A = []
    for _ in range(Q):
        query = input().split()
        if query[0] == '1':
            x = int(query[1])
            A.insert(bisect_left(A, x), x)
        elif query[0] == '2':
            x, k = int(query[1]), int(query[2])
            if k > len(A) or A[-1] <= x:
                print(-1)
            else:
                print(A[bisect_left(A, x, hi=len(A)-k+1)-1])
        else:
            x, k = int(query[1]), int(query[2])
            if k > len(A) or A[0] >= x:
                print(-1)
            else:
                print(A[bisect_right(A, x, lo=k)-1])
main()

=======
Suggestion 6

def insert(x):
    global a
    a.append(x)

=======
Suggestion 7

def main():
    q = int(input())
    
    arr = []
    for i in range(q):
        query = input().split()
        if query[0] == '1':
            arr.append(int(query[1]))
        elif query[0] == '2':
            x = int(query[1])
            k = int(query[2])
            arr.sort(reverse=True)
            cnt = 0
            for j in range(len(arr)):
                if arr[j] <= x:
                    cnt += 1
                if cnt == k:
                    print(arr[j])
                    break
            else:
                print(-1)
        else:
            x = int(query[1])
            k = int(query[2])
            arr.sort()
            cnt = 0
            for j in range(len(arr)):
                if arr[j] >= x:
                    cnt += 1
                if cnt == k:
                    print(arr[j])
                    break
            else:
                print(-1)

=======
Suggestion 8

def main():
    n = int(input())
    a = []
    for i in range(n):
        s = input().split()
        if s[0] == '1':
            a.append(int(s[1]))
        elif s[0] == '2':
            x = int(s[1])
            k = int(s[2])
            b = [i for i in a if i <= x]
            b.sort()
            if len(b) >= k:
                print(b[-k])
            else:
                print(-1)
        elif s[0] == '3':
            x = int(s[1])
            k = int(s[2])
            b = [i for i in a if i >= x]
            b.sort()
            if len(b) >= k:
                print(b[k-1])
            else:
                print(-1)

=======
Suggestion 9

def main():
    n = int(input())
    a = []
    for i in range(n):
        query = input()
        if query[0] == '1':
            a.append(int(query[2:]))
        elif query[0] == '2':
            x = int(query[2:query.find(' ', 2)])
            k = int(query[query.find(' ', 2)+1:])
            b = [i for i in a if i <= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b)[-k])
        else:
            x = int(query[2:query.find(' ', 2)])
            k = int(query[query.find(' ', 2)+1:])
            b = [i for i in a if i >= x]
            if len(b) < k:
                print(-1)
            else:
                print(sorted(b)[k-1])

=======
Suggestion 10

def main():
    pass
