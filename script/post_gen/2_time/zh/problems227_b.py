Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        a = 1
        while a * a <= S[i]:
            if S[i] % a == 0:
                b = S[i] // a
                if 4 * a * b + 3 * a + 3 * b == S[i]:
                    break
            a += 1
        if a * a > S[i]:
            count += 1
    print(count)

=======
Suggestion 2

def main():
    #n = int(input())
    #s = list(map(int, input().split()))
    n = 5
    s = [666,777,888,777,666]
    ans = 0
    for i in range(n):
        if s[i] % 2 == 0:
            ans += 1
        if s[i] % 3 == 2:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in range(n):
        a = 1
        b = 1
        while 4*a*b+3*a+3*b<s[i]:
            if a==b:
                b+=1
            else:
                a+=1
        if 4*a*b+3*a+3*b!=s[i]:
            count+=1
    print(count)

=======
Suggestion 4

def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        for j in range(1, S[i] + 1):
            if (4 * j * (S[i] - j) + 3 * j + 3 * (S[i] - j)) == S[i]:
                break
            elif j == S[i]:
                count += 1
    print(count)

=======
Suggestion 5

def solve():
    # n = int(input())
    # s = list(map(int, input().split()))

    n = 5
    s = [666, 777, 888, 777, 666]

    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                count += 1
    print(count)

=======
Suggestion 6

def main():
    N = int(input())
    S = list(map(int, input().split()))
    result = 0
    for i in range(N):
        a = 1
        while True:
            b = (S[i] - 3 * a) / (4 * a + 3)
            if b < 1:
                break
            if b.is_integer():
                result += 1
                break
            a += 1
    print(N - result)

=======
Suggestion 7

def main():
    n = int(input())
    s = list(map(int, input().split()))
    count = 0
    for i in s:
        if i % 2 == 0:
            if i % 4 != 0:
                count += 1
        else:
            count += 1
    print(count)

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        a = 1
        while a * a <= S[i]:
            if S[i] % a == 0:
                b = S[i] // a
                if 4 * a * b + 3 * a + 3 * b != S[i]:
                    count += 1
            a += 1
    print(count)

=======
Suggestion 9

def main():
    n = int(input())
    s = list(map(int,input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if s[i] == s[j]:
                ans += 1
    print(ans)
main()

=======
Suggestion 10

def main():
    num = int(input())
    guess = list(map(int, input().split()))
    area = []
    for i in range(1, 1000):
        for j in range(1, 1000):
            area.append(4*i*j+3*i+3*j)
    for i in range(num):
        if guess[i] not in area:
            print(i+1)
            break
