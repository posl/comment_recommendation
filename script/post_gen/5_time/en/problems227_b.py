Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    if S[0] + S[1] + S[2] == S[3] + S[4]:
        print(0)
    elif S[0] + S[1] + S[2] < S[3] + S[4]:
        print(0)
    elif S[0] + S[1] + S[2] > S[3] + S[4]:
        print(S[0] + S[1] + S[2] - S[3] - S[4])

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    if S[0] + S[1] + S[2] == S[3] + S[4]:
        print(2)
    elif S[0] + S[1] + S[2] + S[3] == S[4]:
        print(1)
    else:
        print(0)

=======
Suggestion 3

def main():
    n = int(input())
    s = list(map(int, input().split()))
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(n):
        if s[i] % 4 == 0:
            a += 1
        elif s[i] % 2 == 0:
            b += 1
        elif s[i] % 4 == 3:
            d += 1
        else:
            c += 1
    if c == 0:
        if a + 1 >= d:
            print('Yes')
        else:
            print('No')
    else:
        if a >= d:
            print('Yes')
        else:
            print('No')

=======
Suggestion 4

def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if s[0] + s[1] + s[2] == s[3] + s[4] and s[0] + s[4] == s[1] + s[3] and s[0] + s[3] == s[1] + s[2]:
        print(1)
    elif s[0] + s[1] + s[2] == s[3] + s[4]:
        print(2)
    elif s[0] + s[4] == s[1] + s[3] or s[0] + s[3] == s[1] + s[2]:
        print(2)
    elif s[0] + s[1] == s[2] + s[3] or s[0] + s[1] == s[2] + s[4] or s[0] + s[1] == s[3] + s[4] or s[0] + s[2] == s[1] + s[3] or s[0] + s[2] == s[1] + s[4] or s[0] + s[2] == s[3] + s[4]:
        print(2)
    elif s[0] + s[1] == s[2] + s[3] + s[4] or s[0] + s[2] == s[1] + s[3] + s[4]:
        print(2)
    elif s[0] + s[1] + s[2] == s[3] or s[0] + s[1] + s[2] == s[4]:
        print(2)
    else:
        print(3)

=======
Suggestion 5

def main():
    n = int(input())
    s = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a = (s[i] - s[j]) / 4
            b = s[i] / a - 3 * a
            if a > 0 and b > 0 and a.is_integer() and b.is_integer():
                print(n - 1)
                return
    print(n)

=======
Suggestion 6

def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if s[-1] < sum(s[:-1]):
        print(0)
    else:
        print(s[-1] - sum(s[:-1]))

=======
Suggestion 7

def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    S.sort()
    if N == 1:
        print(1)
        exit()
    if N == 2:
        if S[0] == S[1]:
            print(0)
        else:
            print(2)
        exit()
    if N == 3:
        if S[0] == S[1] and S[1] == S[2]:
            print(0)
        elif S[0] == S[1] or S[1] == S[2]:
            print(1)
        else:
            print(3)
        exit()
    if N == 4:
        if S[0] == S[1] and S[1] == S[2] and S[2] == S[3]:
            print(0)
        elif S[0] == S[1] and S[1] == S[2]:
            print(1)
        elif S[1] == S[2] and S[2] == S[3]:
            print(1)
        elif S[0] == S[1] and S[2] == S[3]:
            print(2)
        else:
            print(2)
        exit()
    if N == 5:
        if S[0] == S[1] and S[1] == S[2] and S[2] == S[3] and S[3] == S[4]:
            print(0)
        elif S[0] == S[1] and S[1] == S[2] and S[3] == S[4]:
            print(1)
        elif S[0] == S[1] and S[2] == S[3] and S[3] == S[4]:
            print(1)
        elif S[0] == S[1] and S[1] == S[2]:
            print(1)
        elif S[1] == S[2] and S[2] == S[3]:
            print(1)
        elif S[2] == S[3] and S[3] == S[4]:
            print(1)
        elif S[0] == S[1] and S[3] == S[4

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    if S[0] == S[1] and S[2] == S[3] and S[4] == S[5] and S[0] + S[2] == S[4]:
        print('YES')
    else:
        print('NO')

=======
Suggestion 9

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if a[-1] < sum(a[:-1]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    N = int(input())
    S = list(map(int, input().split()))

    #print(N)
    #print(S)

    a = 0
    b = 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            a = S[i] - S[j]
            if a < 0:
                a = a * -1
            for k in range(N):
                if i == k or j == k:
                    continue
                b = S[i] - S[k]
                if b < 0:
                    b = b * -1
                if a + b == 0:
                    print('No')
                    return
    print('Yes')
    return
