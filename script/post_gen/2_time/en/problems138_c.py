Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = (v[0] + v[1]) / 2
    for i in range(2, n):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = (v[0] + v[1]) / 2
    for i in range(2, N):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, N):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(n - 1):
        v[i + 1] = (v[i] + v[i + 1]) / 2
    print(v[n - 1])

=======
Suggestion 5

def main():
    n = int(input())
    vs = list(map(int, input().split()))
    vs.sort()
    ans = vs[0]
    for i in range(1, n):
        ans = (ans + vs[i]) / 2
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(n-1):
        v[i+1] = (v[i]+v[i+1])/2
    print(v[-1])

=======
Suggestion 7

def main():
    N = int(input())
    V = [int(x) for x in input().split()]

    V.sort()
    ans = V[0]
    for i in range(1, N):
        ans = (ans + V[i]) / 2
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    v.append(0)
    for i in range(N-1):
        v.append((v[i] + v[i+1]) / 2)
    print(v[-1])
