Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    P = list(map(int, input().split()))
    S = [chr(ord('a') + (p - 1)) for p in P]
    print(''.join(S))

=======
Suggestion 2

def main():
    P = [int(x) for x in input().split()]
    S = [chr(ord('a') + (p - 1)) for p in P]
    print("".join(S))

=======
Suggestion 3

def main():
    p = list(map(int,input().split()))
    ans = []
    for i in p:
        ans.append(chr(96+i))
    print(''.join(ans))

=======
Suggestion 4

def main():
    P = list(map(int, input().split()))
    S = [chr(ord('a') + x - 1) for x in P]
    print(''.join(S))

=======
Suggestion 5

def main():
    p = list(map(int, input().split()))
    ans = [None] * 26
    for i in range(26):
        ans[p[i] - 1] = chr(ord('a') + i)
    print(''.join(ans))

=======
Suggestion 6

def main():
    P = list(map(int, input().split()))
    alp = [chr(i) for i in range(97, 97+26)]
    ans = ""
    for i in range(26):
        ans += alp[P[i]-1]
    print(ans)

=======
Suggestion 7

def main():
    p = list(map(int, input().split()))
    s = [None] * 26
    for i in range(26):
        s[i] = chr(ord('a') + p[i] - 1)
    print(''.join(s))

=======
Suggestion 8

def main():
    P = list(map(int, input().split()))
    S = [chr(ord('a') + p - 1) for p in P]
    print(''.join(S))

=======
Suggestion 9

def main():
    P = list(map(int, input().split()))
    S = [chr(96 + p) for p in P]
    print("".join(S))

=======
Suggestion 10

def main():
    p = list(map(int, input().split()))
    s = [chr(96 + i) for i in p]
    print("".join(s))
