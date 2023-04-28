Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, N):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 3

def solve():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(N-1):
        v[i+1] = (v[i]+v[i+1])/2
    print(v[N-1])

=======
Suggestion 5

def main():
    N = int(input())
    v = [int(x) for x in input().split()]
    v.sort()
    for i in range(N-1):
        v[i+1] = (v[i] + v[i+1]) / 2
    print(v[-1])

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    print((v[0]+v[1])/2)
    for i in range(2, n):
        print((v[0]+v[i])/2)
    return

=======
Suggestion 7

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    if N == 2:
        print((v[0]+v[1])/2)
    else:
        for i in range(N-1):
            v[i+1] = (v[i]+v[i+1])/2
        print(v[N-1])

=======
Suggestion 8

def main():
    n = int(input())
    vl = list(map(int, input().split()))
    vl.sort()
    for i in range(1, n):
        vl[i] = (vl[i] + vl[i-1]) / 2
    print(vl[n-1])
