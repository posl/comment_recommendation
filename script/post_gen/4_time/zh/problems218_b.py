Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    p = list(map(int, input().split()))
    print(''.join(list(map(lambda x: chr(x + 96), p))))

=======
Suggestion 2

def main():
    p = list(map(int, input().split()))
    s = list(range(97, 123))
    for i in range(26):
        s[i] = chr(s[i])
    for i in range(26):
        s[p[i] - 1] = chr(97 + i)
    print(''.join(s))

=======
Suggestion 3

def main():
    p = list(map(int, input().split()))
    s = [chr(96+p[i]) for i in range(26)]
    print(''.join(s))

=======
Suggestion 4

def main():
    p = list(map(int, input().split()))
    s = [0] * 26
    for i in range(26):
        s[i] = chr(p[i] + 96)
    print(''.join(s))

=======
Suggestion 5

def main():
    p = list(map(int, input().split()))
    s = [chr(ord('a') + i - 1) for i in p]
    print("".join(s))

=======
Suggestion 6

def solve():
    P = list(map(int, input().split()))
    S = [chr(i+96) for i in P]
    print(''.join(S))

=======
Suggestion 7

def main():
    P = input().split(" ")
    S = ""
    for i in range(26):
        S += chr(int(P[i]) + ord("a") - 1)
    print(S)

=======
Suggestion 8

def problems218_b():
    print("")

=======
Suggestion 9

def main():
    #print('Start...')
    p = list(map(int, input().split()))
    #print(p)
    #print(type(p))
    #print(p[0])
    #print(p[25])
    #print(chr(97))
    #print(chr(65))
    #print(ord('a'))
    #print(ord('z'))
    for i in range(26):
        #print(p[i])
        #print(chr(p[i]+96))
        print(chr(p[i]+96), end='')
    print()

=======
Suggestion 10

def main():
    P = input().split()
    print(P)
    for i in range(len(P)):
        P[i] = int(P[i])
    print(P)
    ans = ""
    for i in range(26):
        ans += chr(P[i] + 96)
    print(ans)
