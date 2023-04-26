Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    d = {}
    for i in range(n):
        l = list(map(int,input().split()))
        l.pop(0)
        d.setdefault(tuple(l),0)
        d[tuple(l)] += 1
    print(len(d))

=======
Suggestion 2

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l.sort(key=lambda x: x[1:])
    cnt = 1
    for i in range(1, n):
        if l[i] != l[i - 1]:
            cnt += 1
    print(cnt)

=======
Suggestion 3

def main():
    n = int(input())
    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))
    l = [tuple(x) for x in l]
    print(len(set(l)))

=======
Suggestion 4

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort()
    #print(L)
    count = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    for i in range(N):
        L, *a = map(int, input().split())
        A.append(a)
    A.sort()
    A.append([])
    ans = 0
    for i in range(N):
        if A[i] != A[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    l = sorted(l, key=lambda x: x[1:])
    ans = 1
    for i in range(n-1):
        if l[i] != l[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    #print(A)
    A.sort()
    #print(A)
    count = 1
    for i in range(1, N):
        if A[i] != A[i-1]:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))
    data.sort()
    #print(data)
    count = 1
    for i in range(N-1):
        if data[i] == data[i+1]:
            continue
        else:
            count += 1
    print(count)

=======
Suggestion 9

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort()
    L.insert(0, [0, 0])
    ans = 1
    for i in range(1, N+1):
        if L[i] != L[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    L = []
    for i in range(N):
        L.append([int(x) for x in input().split()])
    L.sort()
    L.append([0,0])
    count = 1
    for i in range(N):
        if L[i] != L[i+1]:
            count += 1
    print(count)
