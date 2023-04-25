Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * Q
    r = [0] * Q
    for i in range(Q):
        l[i], r[i] = map(int, input().split())
        l[i] -= 1
        r[i] -= 1

    #print(N, Q)
    #print(S)
    #print(l)
    #print(r)

    #ACの出現回数を求める
    AC = [0] * N
    for i in range(1, N):
        if S[i - 1] == "A" and S[i] == "C":
            AC[i] = AC[i - 1] + 1
        else:
            AC[i] = AC[i - 1]

    #print(AC)

    #クエリごとにACの出現回数を求める
    for i in range(Q):
        print(AC[r[i]] - AC[l[i]])

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(1, N):
        if S[i - 1] + S[i] == "AC":
            l[i + 1] = l[i] + 1
        else:
            l[i + 1] = l[i]
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i] - l[l_i])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * N
    for i in range(1, N):
        l[i] = l[i-1]
        if S[i-1] == 'A' and S[i] == 'C':
            l[i] += 1
    for i in range(Q):
        left, right = map(int, input().split())
        print(l[right-1] - l[left-1])

=======
Suggestion 4

def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * n
    for i in range(1, n):
        if s[i - 1:i + 1] == "AC":
            l[i] = l[i - 1] + 1
        else:
            l[i] = l[i - 1]
    for _ in range(q):
        a, b = map(int, input().split())
        print(l[b - 1] - l[a - 1])

=======
Suggestion 5

def main():
    n, q = map(int, input().split())
    s = input()
    l = [0] * (n + 1)
    for i in range(n):
        l[i + 1] = l[i] + (1 if s[i:i + 2] == 'AC' else 0)
    for _ in range(q):
        a, b = map(int, input().split())
        print(l[b - 1] - l[a - 1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * (N + 1)
    for i in range(N - 1):
        if S[i] == 'A' and S[i + 1] == 'C':
            l[i + 2] = l[i + 1] + 1
        else:
            l[i + 2] = l[i + 1]
    for _ in range(Q):
        left, right = map(int, input().split())
        print(l[right] - l[left])

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    s = input()
    l = [0]
    for i in range(1, n):
        if s[i - 1:i + 1] == 'AC':
            l.append(l[i - 1] + 1)
        else:
            l.append(l[i - 1])
    for _ in range(q):
        a, b = map(int, input().split())
        print(l[b - 1] - l[a - 1])

=======
Suggestion 8

def main():
    n, q = map(int, input().split())
    s = input()
    l = []
    for i in range(n-1):
        if s[i:i+2] == "AC":
            l.append(1)
        else:
            l.append(0)
    for i in range(q):
        li, ri = map(int, input().split())
        print(sum(l[li-1:ri-1]))

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * N
    for i in range(N-1):
        if S[i] == "A" and S[i+1] == "C":
            l[i+1] = l[i] + 1
        else:
            l[i+1] = l[i]
    for _ in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i-1] - l[l_i-1])

=======
Suggestion 10

def main():
    n,q = map(int,input().split())
    s = input()
    ac = [0] * (n+1)
    for i in range(n):
        ac[i+1] = ac[i] + (1 if s[i:i+2] == 'AC' else 0)
    for _ in range(q):
        l,r = map(int,input().split())
        print(ac[r-1] - ac[l-1])
