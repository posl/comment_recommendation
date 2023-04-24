Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    diff = [abs(A - (T - h * 0.006)) for h in H]
    print(diff.index(min(diff)) + 1)

=======
Suggestion 2

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    for i in range(n):
        h[i] = abs(a - t + h[i] * 0.006)
    print(h.index(min(h)) + 1)

=======
Suggestion 3

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if abs(A - (T - H[i] * 0.006)) < abs(A - (T - H[ans] * 0.006)):
            ans = i
    print(ans + 1)

=======
Suggestion 4

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    diff = 10**9
    for i in range(N):
        if abs(T-H[i]*0.006-A) < diff:
            diff = abs(T-H[i]*0.006-A)
            ans = i+1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    temp = [T - H_i * 0.006 for H_i in H]
    dist = [abs(A - temp_i) for temp_i in temp]
    print(dist.index(min(dist)) + 1)

=======
Suggestion 6

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    diff = 10**10
    for i in range(N):
        if abs(A - (T - H[i] * 0.006)) < diff:
            diff = abs(A - (T - H[i] * 0.006))
            ans = i + 1
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    min_diff = 1000000000
    for i in range(n):
        diff = abs(a - (t - h[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            ans = i + 1
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    T = T - A
    ans = 0
    min = 100
    for i in range(N):
        if min > abs(T - H[i] * 0.006):
            min = abs(T - H[i] * 0.006)
            ans = i + 1
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    T = T - A

    ans = 0
    min = 1000000000
    for i in range(N):
        if abs(T - H[i] * 0.006) < min:
            ans = i + 1
            min = abs(T - H[i] * 0.006)

    print(ans)

=======
Suggestion 10

def main():
    #入力
    n = int(input())
    t,a = map(int,input().split())
    h = list(map(int,input().split()))
    #平均気温をリスト化
    temp = [t-h[i]*0.006 for i in range(n)]
    #平均気温と目標気温の差をリスト化
    diff = [abs(temp[i]-a) for i in range(n)]
    #最小値を出力
    print(diff.index(min(diff))+1)
