Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, N):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()
    ans = v[0]
    for i in range(1, n):
        ans = (ans + v[i]) / 2
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(N-1):
        v[i+1] = (v[i] + v[i+1]) / 2
    print(v[-1])

=======
Suggestion 4

def main():
    N = int(input())
    v = list(map(int,input().split()))
    v.sort()
    for i in range(N-1):
        v[i+1] = (v[i]+v[i+1])/2
    print(v[N-1])

=======
Suggestion 5

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(1, N):
        v[i] = (v[i] + v[i-1]) / 2
    print(v[-1])

=======
Suggestion 6

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    while len(v) > 1:
        v1 = v.pop(0)
        v2 = v.pop(0)
        v.append((v1 + v2) / 2)
        v.sort()
    print(v[0])

=======
Suggestion 7

def main():
    N = int(input())
    v = list(map(int, input().split()))
    v.sort()
    for i in range(N - 1):
        v.append((v[i] + v[i + 1]) / 2)
        v.sort()
    print(v[-1])

=======
Suggestion 8

def main():
    # 入力
    N = int(input())
    v = list(map(int, input().split()))

    # 結果出力
    print(sum(v) / N)
