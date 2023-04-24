Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans = abs(A - (T - H[i] * 0.006))
        else:
            if ans > abs(A - (T - H[i] * 0.006)):
                ans = abs(A - (T - H[i] * 0.006))
                ans_i = i
    print(ans_i + 1)

=======
Suggestion 2

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0:
            ans = abs(t - h[i] * 0.006 - a)
        else:
            if abs(t - h[i] * 0.006 - a) < ans:
                ans = abs(t - h[i] * 0.006 - a)
                index = i
    print(index + 1)

=======
Suggestion 3

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    diff = 1000
    for i in range(N):
        tmp = T - H[i]*0.006
        if abs(tmp - A) < diff:
            diff = abs(tmp - A)
            ans = i + 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = 10**9
    for i in range(N):
        temp = T - H[i]*0.006
        diff = abs(temp - A)
        if diff < min_diff:
            ans = i+1
            min_diff = diff
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min_diff = abs(A - (T - H[0] * 0.006))
    for i in range(1, N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            min_diff = diff
            ans = i
    print(ans + 1)

=======
Suggestion 6

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 1000
    for i in range(n):
        if abs(a - (t - h[i] * 0.006)) < min:
            min = abs(a - (t - h[i] * 0.006))
            ans = i
    print(ans + 1)

=======
Suggestion 7

def main():
    #input
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    #compute
    #output
    print(H.index(min(H, key=lambda x: abs(A-T+0.006*x)))+1)

=======
Suggestion 8

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min_d = 100000000
    min_i = 0
    for i in range(n):
        d = abs(a - (t - h[i] * 0.006))
        if min_d > d:
            min_d = d
            min_i = i
    print(min_i + 1)

=======
Suggestion 9

def main():
    # read data
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))

    # solve
    ans = 1
    min_diff = abs(T - H[0] * 0.006 - A)
    for i in range(1, N):
        diff = abs(T - H[i] * 0.006 - A)
        if diff < min_diff:
            ans = i + 1
            min_diff = diff

    # output
    print(ans)

=======
Suggestion 10

def main():
    #input
    N = int(input())
    T, A = map(int,input().split())
    H = list(map(int,input().split()))
    #calc
    ans = 1
    for i in range(2,N+1):
        if abs(T - H[ans-1]*0.006 - A) > abs(T - H[i-1]*0.006 - A):
            ans = i
    #output
    print(ans)
