Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    P = list(map(int, input().split()))
    S = "abcdefghijklmnopqrstuvwxyz"
    T = [0]*26
    for i in range(26):
        T[P[i]-1] = S[i]
    print("".join(T))

=======
Suggestion 2

def main():
    p = list(map(int, input().split()))
    s = ""
    for i in range(26):
        s += chr(p.index(i + 1) + 97)
    print(s)

=======
Suggestion 3

def main():
    P = input().split()
    P = [int(i) for i in P]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    S = ""
    for i in range(26):
        S += alphabet[P[i]-1]
    print(S)

=======
Suggestion 4

def main():
    P = [int(i) for i in input().split()]
    S = [chr(97+i-1) for i in P]
    print("".join(S))

=======
Suggestion 5

def main():
    P = input().split()
    S = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(S[int(P[i])-1], end="")
    print()

=======
Suggestion 6

def main():
    p = [int(x) for x in input().split()]
    s = [chr(97+i) for i in range(26)]
    t = [0]*26
    for i in range(26):
        t[p[i]-1] = s[i]
    print(''.join(t))

=======
Suggestion 7

def main():
    #input
    Ps = list(map(int, input().split()))
    #compute
    S = ''
    for i in range(26):
        S += chr(ord('a')+Ps[i]-1)
    #output
    print(S)

=======
Suggestion 8

def main():
    #input
    P = list(map(int, input().split()))
    #compute
    ans = ['a']*26
    for i in range(26):
        ans[P[i]-1] = chr(97+i)
    #output
    print(''.join(ans))

=======
Suggestion 9

def main():
    P = input().split()
    S = ""
    for p in P:
        S += chr(96 + int(p))
    print(S)

=======
Suggestion 10

def main():
    #input
    P = list(map(int, input().split()))
    
    #compute
    S = [chr(97+i) for i in range(26)]
    for i in range(26):
        S[i],S[P[i]-1] = S[P[i]-1],S[i]
    
    #output
    print(''.join(S))
