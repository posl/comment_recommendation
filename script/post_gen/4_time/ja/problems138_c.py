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

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(n-1):
        v[i+1] = (v[i]+v[i+1])/2
    print(v[n-1])

=======
Suggestion 4

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, len(v)):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(n-1):
        v[i+1] = (v[i] + v[i+1])/2
    print(v[-1])

=======
Suggestion 6

def solve():
    N = int(input())
    v_list = list(map(int, input().split()))

    v_list.sort()
    ans = v_list[0]
    for i in range(1, N):
        ans = (ans + v_list[i]) / 2

    print(ans)
