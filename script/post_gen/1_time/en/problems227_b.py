Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if 4 * s[i] + 3 * s[j] == 3 * s[i] + 4 * s[j]:
                print("YES")
                return
    print("NO")

=======
Suggestion 2

def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    if n == 1:
        print(1)
    elif n == 2:
        if s[0] == s[1]:
            print(1)
        else:
            print(2)
    else:
        if s[0] == s[1]:
            print(n-1)
        elif s[1] == s[2]:
            print(n-1)
        elif s[0] == s[2]:
            print(n-1)
        else:
            print(n)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    if a[0] + a[1] == a[2]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def solve():
    n = int(input())
    s = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i, n):
            if s[i] > s[j]:
                s[i], s[j] = s[j], s[i]
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                if s[i] + s[j] > s[k]:
                    ans += 1
    print(ans)

=======
Suggestion 5

def main():
    n = int(input())
    s = input().split()
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(n):
        if int(s[i]) % 4 == 0:
            a += 1
        elif int(s[i]) % 2 == 0:
            b += 1
        elif int(s[i]) % 4 == 3:
            d += 1
        else:
            c += 1
    if d == 0:
        if a >= c - 1:
            print('Yes')
        else:
            print('No')
    else:
        if a >= c:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    n = int(input())
    s = [int(x) for x in input().split()]
    s.sort()
    if s[-1] > sum(s[:-1]):
        print('No')
    else:
        print('Yes')

=======
Suggestion 7

def main():
    N = int(input())
    S = list(map(int, input().split()))
    if (4 * min(S) + 3 * S.index(min(S)) + 3 * (N - S.index(min(S)) - 1)) <= max(S):
        print(0)
    else:
        print(N - 1)

=======
Suggestion 8

def main():
    N = int(input())
    S = [int(x) for x in input().split()]
    result = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] + S[j] == 777:
                result += 1
    print(result)

=======
Suggestion 9

def main():
    N = int(input())
    S = list(map(int, input().split()))
    for i in range(N):
        S[i] -= 3
    S.sort()
    cnt = 0
    for i in range(N):
        if S[i] <= 0:
            continue
        cnt += 1
        for j in range(i+1, N):
            if S[j] % S[i] == 0:
                S[j] = 0
    print(cnt)

=======
Suggestion 10

def get_input():
    num = int(input())
    s_list = list(map(int, input().split()))
    return num, s_list
