Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    ans = 0
    for i in range(n):
        ans += a[i] / b[i]
    ans /= 2
    print(ans)

=======
Suggestion 2

def solve():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    l = 0
    r = 10**9
    while r-l > 10**-5:
        m = (l+r)/2
        t = 0
        for i in range(n):
            t += a[i]/(b[i]+m)
        if t > m:
            l = m
        else:
            r = m
    print(l)

=======
Suggestion 3

def get_input():
    N = int(input())
    A, B = [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    return N, A, B

=======
Suggestion 4

def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    left = 0
    right = 0
    for i in range(n):
        left += a[i] / b[i]
    for i in range(n):
        right += a[i] / b[n - i - 1]
    print(left/2 + right/2)

=======
Suggestion 5

def main():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a,b = map(int, input().split())
        A.append(a)
        B.append(b)
    left = 0
    right = 0
    for i in range(N):
        left += A[i] / B[i]
    for i in range(N):
        right += A[i] / B[i]
    right /= 2
    while True:
        tmp = 0
        for i in range(N):
            tmp += A[i] / B[i]
        if left < right:
            left = right
            right = (left + tmp) / 2
        else:
            right = left
            left = (right + tmp) / 2
        if abs(left - right) < 0.000000000000001:
            break
    print(left)

=======
Suggestion 6

def solve():
    N = int(input())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    print(sum(A[i] / B[i] for i in range(N)) / 2)

=======
Suggestion 7

def get_input():
    N = int(input())
    A = []
    B = []
    for i in range(N):
        line = input()
        A.append(int(line.split()[0]))
        B.append(int(line.split()[1]))
    return N, A, B

=======
Suggestion 8

def main():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    l = 0
    r = 1000000
    while r - l > 1e-6:
        m = (r + l) / 2
        t = 0
        for a, b in AB:
            t += a / (m / b)
        if t >= 2:
            l = m
        else:
            r = m
    print(l)

=======
Suggestion 9

def main():
    n = int(input())
    a_b = []
    for _ in range(n):
        a_b.append(list(map(int, input().split())))
    a_b.sort(key=lambda x: x[0])
    # print(a_b)
    total_length = sum([x[0] for x in a_b])
    half_length = total_length / 2
    # print(total_length, half_length)
    current_length = 0
    current_speed = 0
    for a, b in a_b:
        current_length += a
        current_speed += b
        if current_length > half_length:
            break
    # print(current_length, current_speed)
    print(current_speed * (current_length - half_length) / current_speed)

=======
Suggestion 10

def fuses(N, A, B):
    #print(N, A, B)
    t = 0
    for i in range(N):
        t += A[i]/B[i]
    #print(t)
    t = t/2
    #print(t)
    d = 0
    for i in range(N):
        d += A[i]*min(1, t*B[i]/A[i])
    #print(d)
    return d
