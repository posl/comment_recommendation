Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    s = input()
    # print(n, x, s)
    for i in range(n):
        if s[i] == 'U':
            x = x // 2
        elif s[i] == 'L':
            x = x * 2
        else:
            x = x * 2 + 1
    print(x)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    s = input()
    #print(n)
    #print(x)
    #print(s)
    #print(2**(10**100)-1)
    #print(10**18)
    #print(2**63-1)
    #print(2**63)
    #print(2**62)
    #print(2**61)
    #print(2**60)
    #print(2**59)
    #print(2**58)
    #print(2**57)
    #print(2**56)
    #print(2**55)
    #print(2**54)
    #print(2**53)
    #print(2**52)
    #print(2**51)
    #print(2**50)
    #print(2**49)
    #print(2**48)
    #print(2**47)
    #print(2**46)
    #print(2**45)
    #print(2**44)
    #print(2**43)
    #print(2**42)
    #print(2**41)
    #print(2**40)
    #print(2**39)
    #print(2**38)
    #print(2**37)
    #print(2**36)
    #print(2**35)
    #print(2**34)
    #print(2**33)
    #print(2**32)
    #print(2**31)
    #print(2**30)
    #print(2**29)
    #print(2**28)
    #print(2**27)
    #print(2**26)
    #print(2**25)
    #print(2**24)
    #print(2**23)
    #print(2**22)
    #print(2**21)
    #print(2**20)
    #print(2**19)
    #print(2**18)
    #print(2**17)
    #print(2**16)
    #print(2**15)
    #print(2**14)
    #print(2**13)
    #print(2**12)
    #print(2**11)
    #print(2**10)
    #print(

=======
Suggestion 3

def get_parent(i):
    return i//2

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'U':
            ans = ans // 2
        elif S[i] == 'L':
            ans = ans * 2 - 1
        elif S[i] == 'R':
            ans = ans * 2 + 1
    print(ans)

=======
Suggestion 5

def solve():
    N,X = map(int,input().split())
    S = input()
    ans = X
    for i in range(N):
        if S[i] == 'U':
            ans //=2
        elif S[i] == 'L':
            ans = ans*2-1
        else:
            ans = ans*2+1
    print(ans)

=======
Suggestion 6

def solve():
    N, X = map(int, input().split())
    S = input()
    answer = X
    for i in range(N):
        if S[i] == "U":
            answer //= 2
        elif S[i] == "L":
            answer = answer * 2 - 1
        else:
            answer = answer * 2 + 1
    print(answer)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'U':
            X = (X + 1) // 2
        elif s == 'L':
            X = 2 * X
        else:
            X = 2 * X + 1
    print(X)

=======
Suggestion 8

def main():
    n,x = map(int,input().split())
    s = input()
    
    for i in range(n):
        if s[i] == "U":
            x = x//2
        elif s[i] == "L":
            x = x*2
        elif s[i] == "R":
            x = x*2+1

    print(x)

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    s = input()
    ans = x
    for i in range(n):
        if s[i] == 'U':
            ans //= 2
        elif s[i] == 'L':
            ans = ans*2 - 1
        else:
            ans = ans*2 + 1
    print(ans)

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    S = input()
    X = bin(X)[2:]
    for s in S:
        if s == 'U':
            X = X[:-1]
        elif s == 'L':
            X = X + '0'
        else:
            X = X + '1'
    print(int(X, 2))
