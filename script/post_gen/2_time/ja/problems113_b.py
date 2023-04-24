Synthesizing 10/10 solutions

=======
Suggestion 1

def get_input():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    return n, t, a, h

=======
Suggestion 2

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    diff = 100000000
    for i in range(n):
        tmp = t - h[i] * 0.006
        if diff > abs(a - tmp):
            ans = i + 1
            diff = abs(a - tmp)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 100000000
    index = 0
    for i in range(n):
        temp = t - h[i] * 0.006
        if abs(a - temp) < min:
            min = abs(a - temp)
            index = i
    print(index + 1)

=======
Suggestion 4

def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    h = [t - i * 0.006 for i in h]

    ans = 0
    ans_temp = 1000000000
    for i in range(n):
        if ans_temp > abs(a - h[i]):
            ans_temp = abs(a - h[i])
            ans = i + 1

    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    t, a = list(map(int, input().split()))
    h = list(map(int, input().split()))
    h = [abs(a - (t - i * 0.006)) for i in h]
    print(h.index(min(h)) + 1)

=======
Suggestion 6

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 0
    min = 1e9
    for i in range(N):
        temp = T - H[i] * 0.006
        if min > abs(A - temp):
            min = abs(A - temp)
            ans = i + 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    H_ave = [abs(T - h * 0.006 - A) for h in H]
    print(H_ave.index(min(H_ave)) + 1)

=======
Suggestion 8

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    min = 100000000
    index = 1
    for i in range(N):
        temp = T - H[i] * 0.006
        if abs(A - temp) < min:
            min = abs(A - temp)
            index = i + 1
    print(index)

=======
Suggestion 9

def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    #print(N, T, A, H)
    temp = 10000000000
    ans = 0
    for i in range(N):
        if temp > abs(A - (T - H[i]*0.006)):
            temp = abs(A - (T - H[i]*0.006))
            ans = i + 1
    print(ans)

=======
Suggestion 10

def get_input_int():
    return int(input())
