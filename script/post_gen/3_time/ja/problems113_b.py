Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    mi

=======
Suggestion 2

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    # 宮殿を建設すべき地点の番号を出力
    print(H.index(min(H, key=lambda x: abs(A - (T - x * 0.006)))))

=======
Suggestion 3

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    d = []
    for i in range(N):
        d.append(abs(A - (T - H[i] * 0.006)))
    print(d.index(min(d)) + 1)

=======
Suggestion 4

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [abs(a - (t - x * 0.006)) for x in h]
    print(h.index(min(h)) + 1)

=======
Suggestion 5

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min = 10**10
    for i in range(N):
        if abs(T - H[i] * 0.006 - A) < min:
            ans = i
            min = abs(T - H[i] * 0.006 - A)
    print(ans + 1)

=======
Suggestion 6

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min = 100000000
    for i in range(N):
        if abs(T - H[i]*0.006 - A) < min:
            min = abs(T - H[i]*0.006 - A)
            ans = i
    print(ans+1)

=======
Suggestion 7

def main():
    N = int(input())
    T,A = map(int,input().split())
    H = list(map(int,input().split()))
    ans = 0
    min = 1000
    for i in range(N):
        if abs(A-(T-H[i]*0.006)) < min:
            ans = i+1
            min = abs(A-(T-H[i]*0.006))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    T = T - A
    ans = 0
    for i in range(N):
        if T - H[i]*0.006 > 0:
            if T - H[i]*0.006 < T - H[ans]*0.006:
                ans = i
        else:
            if T - H[i]*0.006 > T - H[ans]*0.006:
                ans = i
    print(ans+1)

=======
Suggestion 9

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min = 1000000000000
    for i in range(N):
        if min > abs(A - (T - H[i] * 0.006)):
            min = abs(A - (T - H[i] * 0.006))
            ans = i + 1
    print(ans)

=======
Suggestion 10

def main():
    n = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    ans = 0
    min_diff = 1000000000
    for i in range(n):
        diff = abs(A-(T-H[i]*0.006))
        if diff < min_diff:
            ans = i + 1
            min_diff = diff

    print(ans)
