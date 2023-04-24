Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    X = 0
    Y = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            X += V[i]
            Y += C[i]
    print(X - Y)

=======
Suggestion 3

def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if v[i] - c[i] > 0:
            ans += v[i] - c[i]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    V = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    X = 0
    Y = 0
    for i in range(N):
        if V[i] > C[i]:
            X += V[i]
            Y += C[i]
    print(X - Y)

=======
Suggestion 6

def main():
    n = int(input())
    v = list(map(int,input().split()))
    c = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        if v[i] > c[i]:
            ans += v[i] - c[i]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    V = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    ans = 0
    for i in range(N):
        if V[i] > C[i]:
            ans += V[i] - C[i]
    print(ans)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    V = list(map(int,input().split()))
    C = list(map(int,input().split()))
    #処理
    ans = 0
    for i in range(N):
        if V[i] - C[i] > 0:
            ans += V[i] - C[i]
    #出力
    print(ans)
