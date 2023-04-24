Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    P = list(map(int, input().split()))
    S = []
    for i in range(26):
        S.append(chr(ord('a') + P[i] - 1))
    print(''.join(S))

=======
Suggestion 2

def main():
    p = list(map(int, input().split()))
    alphabet = [chr(ord('a') + i - 1) for i in p]
    print(''.join(alphabet))

=======
Suggestion 3

def main():
    P = list(map(int, input().split()))
    S = [chr(ord('a') + p - 1) for p in P]
    print(''.join(S))

=======
Suggestion 4

def main():
    P = list(map(int, input().split()))
    S = []
    for i in range(26):
        S.append(chr(P[i]+96))
    print(''.join(S))

=======
Suggestion 5

def main():
    p = list(map(int, input().split()))
    ans = ""
    for i in range(26):
        ans += chr(p[i] + 96)
    print(ans)

=======
Suggestion 6

def main():
    p = list(map(int, input().split()))
    p = [chr(ord('a') + i - 1) for i in p]
    print(''.join(p))

=======
Suggestion 7

def main():
    P = list(map(int, input().split()))
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    for i in P:
        ans += alphabet[i-1]
    print(ans)
main()

=======
Suggestion 8

def main():
    p = list(map(int, input().split()))
    for i in range(26):
        print(chr(p[i]+96), end="")
    print()

=======
Suggestion 9

def main():
    p = list(map(int,input().split()))
    p = [chr(ord('a') + p[i] - 1) for i in range(26)]
    print(''.join(p))

=======
Suggestion 10

def main():
    p_list = list(map(int, input().split()))
    a_list = [chr(96 + p) for p in p_list]
    print(''.join(a_list))
