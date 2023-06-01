Synthesizing 10/10 solutions

=======
Suggestion 1

def problem123_b():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    M = min(A,B,C,D,E)
    if A%M==0:
        A = A
    else:
        A = A + M - A%M
    if B%M==0:
        B = B
    else:
        B = B + M - B%M
    if C%M==0:
        C = C
    else:
        C = C + M - C%M
    if D%M==0:
        D = D
    else:
        D = D + M - D%M
    if E%M==0:
        E = E
    else:
        E = E + M - E%M
    print(A+B+C+D+E)

problem123_b()

=======
Suggestion 2

def main():
    #读取输入
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #计算答案
    ans = 0
    if A % 10 != 0:
        ans += (A // 10 + 1) * 10
    else:
        ans += A
    if B % 10 != 0:
        ans += (B // 10 + 1) * 10
    else:
        ans += B
    if C % 10 != 0:
        ans += (C // 10 + 1) * 10
    else:
        ans += C
    if D % 10 != 0:
        ans += (D // 10 + 1) * 10
    else:
        ans += D
    if E % 10 != 0:
        ans += (E // 10 + 1) * 10
    else:
        ans += E
    #输出结果
    print(ans)

=======
Suggestion 3

def main():
    A, B, C, D, E = map(int, open(0).read().split())
    print((A - 1) // 10 * 10 + A + (B - 1) // 10 * 10 + B + (C - 1) // 10 * 10 + C + (D - 1) // 10 * 10 + D + (E - 1) // 10 * 10 + E)

=======
Suggestion 4

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    min_time = 10**9
    for i in [A,B,C,D,E]:
        if i%10 != 0:
            min_time = min(min_time,i%10)
    print(10*(A//10+B//10+C//10+D//10+E//10)+min_time-10)

=======
Suggestion 5

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    # print(A)
    # print(B)
    # print(C)
    # print(D)
    # print(E)
    time = 0
    time += (A % 10) * 10
    time += (B % 10) * 10
    time += (C % 10) * 10
    time += (D % 10) * 10
    time += (E % 10) * 10
    print(time)

=======
Suggestion 6

def problem123_b():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    ans = 0
    if a % 10 != 0:
        a = a + (10 - a % 10)
    if b % 10 != 0:
        b = b + (10 - b % 10)
    if c % 10 != 0:
        c = c + (10 - c % 10)
    if d % 10 != 0:
        d = d + (10 - d % 10)
    if e % 10 != 0:
        e = e + (10 - e % 10)
    if a >= b and a >= c and a >= d and a >= e:
        ans = ans + a
    elif b >= a and b >= c and b >= d and b >= e:
        ans = ans + b
    elif c >= a and c >= b and c >= d and c >= e:
        ans = ans + c
    elif d >= a and d >= b and d >= c and d >= e:
        ans = ans + d
    elif e >= a and e >= b and e >= c and e >= d:
        ans = ans + e
    print(ans)

=======
Suggestion 7

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    a = A
    b = B
    c = C
    d = D
    e = E
    if A % 10 != 0:
        A = A + (10 - (A % 10))
    if B % 10 != 0:
        B = B + (10 - (B % 10))
    if C % 10 != 0:
        C = C + (10 - (C % 10))
    if D % 10 != 0:
        D = D + (10 - (D % 10))
    if E % 10 != 0:
        E = E + (10 - (E % 10))
    print(A + B + C + D + E - 10 - max(A, B, C, D, E))
    return 0

=======
Suggestion 8

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    if a % 10 == 0:
        a = a
    else:
        a = a + (10 - a % 10)
    if b % 10 == 0:
        b = b
    else:
        b = b + (10 - b % 10)
    if c % 10 == 0:
        c = c
    else:
        c = c + (10 - c % 10)
    if d % 10 == 0:
        d = d
    else:
        d = d + (10 - d % 10)
    if e % 10 == 0:
        e = e
    else:
        e = e + (10 - e % 10)
    print(a + b + c + d + e)

=======
Suggestion 9

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    #print(A, B, C, D, E)
    #print(type(A), type(B), type(C), type(D), type(E))
    #print(10*round(A/10), 10*round(B/10), 10*round(C/10), 10*round(D/10), 10*round(E/10))
    print(10*round(A/10)+10*round(B/10)+10*round(C/10)+10*round(D/10)+10*round(E/10)-50)

=======
Suggestion 10

def get_min_time(a, b, c, d, e):
    time = [a, b, c, d, e]
    min_time = 0
    for i in range(5):
        if time[i] % 10 != 0:
            time[i] = time[i] + 10 - time[i] % 10
    min_time = max(time)
    return min_time
