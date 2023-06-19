Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        l = list(map(int, input().split()))
        l.pop(0)
        a[i] = tuple(l)
    print(len(set(a)))
    return

=======
Suggestion 2

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x: x[1:])
    ans = 1
    for i in range(1, n):
        if a[i] != a[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    d = {}
    for i in range(n):
        a[i].pop(0)
        d.setdefault(tuple(a[i]), 0)
        d[tuple(a[i])] += 1
    print(len(d))

=======
Suggestion 4

def main():
    n = int(input())
    seq = []
    for i in range(n):
        seq.append([int(x) for x in input().split()])
    print(len(set(tuple(x) for x in seq)))

=======
Suggestion 5

def main():
    N = int(input())
    d = {}
    for i in range(N):
        L = int(input().split()[0])
        s = input().split()
        if L == 1:
            if s[0] in d.keys():
                d[s[0]] += 1
            else:
                d[s[0]] = 1
        else:
            if s[0] in d.keys():
                d[s[0]] += 1
            else:
                d[s[0]] = 1
            if s[-1] in d.keys():
                d[s[-1]] += 1
            else:
                d[s[-1]] = 1
    print(len(d.keys()))

=======
Suggestion 6

def solve():
    N = int(input())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    L.sort()
    ans = 1
    for i in range(N-1):
        if L[i] != L[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def readinput():
    n = int(input())
    L = []
    for i in range(n):
        l = list(map(int, input().split()))
        L.append(l)
    return n, L

=======
Suggestion 8

def main():
    n = int(input())
    dic = {}
    for _ in range(n):
        line = input().split()
        line = [int(i) for i in line]
        if line[0] not in dic:
            dic[line[0]] = set()
        dic[line[0]].add(tuple(line[1:]))
    print(len(dic))

=======
Suggestion 9

def main():
    N = int(input())
    L = []
    for i in range(N):
        a = list(map(int, input().split()))
        L.append(a)
    result = 1
    for i in range(N):
        for j in range(i + 1, N):
            if L[i] == L[j]:
                break
            if j == N - 1:
                result += 1
    print(result)

=======
Suggestion 10

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split()))[1:])
    a.sort()
    ans = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            ans += 1
    print(ans)
