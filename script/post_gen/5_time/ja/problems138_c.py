Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
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
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 4

def cal_average(a,b):
    return (a+b)/2

n = int(input())
v = list(map(int,input().split()))

for i in range(n-1):
    v.sort()
    v[0] = cal_average(v[0],v[1])
    v.pop(1)

print(v[0])

=======
Suggestion 5

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    while len(v) > 1:
        v.append((v.pop(0) + v.pop(0)) / 2)
    print(v[0])

=======
Suggestion 6

def solve():
    N = int(input())
    V = list(map(int, input().split()))

    V.sort()
    ans = V[0]
    for i in range(1, N):
        ans = (ans + V[i]) / 2

    return ans

print(solve())

=======
Suggestion 7

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(n-1):
        v[i+1] = (v[i] + v[i+1]) / 2
    print(v[n-1])

=======
Suggestion 8

def get_input():
    n = int(input())
    v = list(map(int, input().split()))
    return n, v
