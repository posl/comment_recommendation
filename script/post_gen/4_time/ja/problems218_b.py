Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    p = list(map(int, input().split()))
    for i in range(26):
        print(chr(ord('a') + p[i] - 1), end='')
    print()

=======
Suggestion 2

def main():
    p = list(map(int, input().split()))
    a = list(map(chr, range(97, 97+26)))
    for i in range(26):
        a[p[i]-1] = chr(97+i)
    print(''.join(a))

=======
Suggestion 3

def main():
    p = list(map(int, input().split()))
    a = [chr(ord('a') + i - 1) for i in p]
    print(''.join(a))

=======
Suggestion 4

def main():
    P = list(map(int, input().split()))
    ans = ""
    for p in P:
        ans += chr(ord("a") + p - 1)
    print(ans)

=======
Suggestion 5

def main():
    p = list(map(int, input().split()))
    s = [chr(ord('a') + i - 1) for i in p]
    print(''.join(s))

=======
Suggestion 6

def main():
    p = list(map(int, input().split()))
    s = [chr(96 + i) for i in p]
    print(''.join(s))

=======
Suggestion 7

def main():
    P = list(map(int,input().split()))
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    ans = ""
    for i in range(len(P)):
        ans += alphabets[P[i]-1]
    print(ans)

=======
Suggestion 8

def main():
    p = list(map(int, input().split()))
    ans = [chr(p[i]+96) for i in range(26)]
    print("".join(ans))

=======
Suggestion 9

def main():
    p = list(map(int,input().split()))
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    ans = ''
    for i in p:
        ans += alpha[i-1]
    print(ans)

=======
Suggestion 10

def main():
    # 文字列の入力
    p = list(map(int, input().split()))
    a = list(map(chr, range(97, 123)))
    ans = ''
    for i in p:
        ans += a[i-1]
    print(ans)
