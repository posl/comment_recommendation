Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def check_palindrome(s):
    if len(s) == 1:
        return True
    else:
        for i in range(int(len(s)/2)):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def problems286_c():
    n, a, b = map(int, input().split())
    s = input()
    if n % 2 == 0:
        if a > b:
            print((a * n) + b)
        else:
            print((a * n) + (b * (n // 2)))
    else:
        if a > b:
            print((a * n) + b)
        else:
            print((a * n) + (b * (n // 2)) + a)

=======
Suggestion 4

def solve():
    N, A, B = map(int, input().split())
    S = input()
    print(N, A, B, S)
    return 0

=======
Suggestion 5

def main():
    N, A, B = map(int, input().split())
    S = input()
    count = 0
    for i in range(N//2):
        if S[i] != S[-i-1]:
            if S[i] == 'a' or S[-i-1] == 'a':
                count += A
            else:
                count += B
    if N % 2 == 1 and S[N//2] == 'a':
        count += A
    print(count)

=======
Suggestion 6

def main():
    n = int(input())
    a, b = map(int, input().split())
    s = input()
    print(n, a, b, s)
    #print(s[0:int(n/2)])
    #print(s[int(n/2):n])
    if s[0:int(n/2)] == s[int(n/2):n]:
        print(a*n+b*n)
    else:
        print(a*n+b*(n+1))

=======
Suggestion 7

def problems286_c():
    pass

=======
Suggestion 8

def is_palindrome(s):
    return s == s[::-1]

=======
Suggestion 9

def main():
    N,A,B = map(int, input().split())
    S = input()

    #print(S)
    #print(N,A,B)

    #判断是否是回文
    def is_huiwen(S):
        if S == S[::-1]:
            return True
        else:
            return False

    #print(is_huiwen(S))

    #判断回文的个数
    def huiwen_count(S):
        count = 0
        for i in range(N//2):
            if S[i] != S[N-i-1]:
                count += 1
        return count

    #print(huiwen_count(S))

    if is_huiwen(S):
        print(A*N+B*(huiwen_count(S)//2))
    else:
        print(A*N+B*huiwen_count(S))
