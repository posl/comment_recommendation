Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if s[0] + s[1] + s[2] == s[3] + s[4]:
        print(0)
    elif s[0] + s[1] + s[2] < s[3] + s[4]:
        print(0)
    elif s[0] + s[1] + s[2] > s[3] + s[4]:
        print(2)
    else:
        print(1)

=======
Suggestion 2

def main():
    N = int(input())
    S = list(map(int, input().split()))
    sum = 0
    for i in range(N):
        sum += S[i]
    if sum % 10 != 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    if S[-1] < sum(S[:-1]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    N = int(input())
    S = list(map(int, input().split()))
    S.sort()
    if (S[0] + S[1] + S[2] == S[3] + S[4]):
        print("YES")
    else:
        print("NO")

=======
Suggestion 5

def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if S[i] == S[j]:
                ans = 1
    if ans == 0:
        print(N)
    else:
        print(N-1)

=======
Suggestion 6

def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    if n == 1:
        print(1)
        exit()
    if n == 2:
        if s[0] == s[1]:
            print(2)
        else:
            print(1)
        exit()
    if n == 3:
        if s[0] + s[1] == s[2]:
            print(1)
            exit()
        else:
            print(2)
            exit()
    if n == 4:
        if s[0] + s[1] == s[2] + s[3]:
            print(2)
            exit()
        if s[0] + s[1] == s[2]:
            print(2)
            exit()
        if s[0] + s[1] == s[3]:
            print(2)
            exit()
        if s[0] + s[2] == s[1] + s[3]:
            print(2)
            exit()
        if s[0] + s[2] == s[1]:
            print(2)
            exit()
        if s[0] + s[2] == s[3]:
            print(2)
            exit()
        if s[0] + s[3] == s[1] + s[2]:
            print(2)
            exit()
        if s[0] + s[3] == s[1]:
            print(2)
            exit()
        if s[0] + s[3] == s[2]:
            print(2)
            exit()
        if s[1] + s[2] == s[0] + s[3]:
            print(2)
            exit()
        if s[1] + s[2] == s[0]:
            print(2)
            exit()
        if s[1] + s[2] == s[3]:
            print(2)
            exit()
        if s[1] + s[3] == s[0] + s[2]:
            print(2)
            exit()
        if s[1] + s[3] == s[0]:
            print(2)
            exit()
        if s[1] + s[3] == s[2]:
            print

=======
Suggestion 7

def main():
    n = int(input())
    s = list(map(int, input().split()))
    if 4*min(s) < sum(s):
        print(0)
    else:
        print(4*min(s) - sum(s))

=======
Suggestion 8

def main():
    N = int(input())
    S = list(map(int, input().split()))

    if sum(S) % 10 != 0:
        print("Yes")
        return

    for i in range(N):
        if S[i] % 10 != 0:
            print("Yes")
            return

    print("No")

=======
Suggestion 9

def main():
    N = int(input())
    S = list(map(int, input().split()))
    a = []
    b = []
    for i in range(N):
        a.append((S[i]+3)/4)
        b.append((S[i]-3)/4)
    if max(a) < min(b):
        print(N)
    elif min(a) > max(b):
        print(0)
    else:
        print(N - (a.index(max(a))+1) - (N - b.index(min(b))))

=======
Suggestion 10

def main():
    n = int(input())
    s = [int(x) for x in input().split()]

    #print(n)
    #print(s)

    #print(s.count(1))

    #print(s.count(4))
    #print(s.count(3))
    #print(s.count(2))
    #print(s.count(1))

    if s.count(4) == 1 and s.count(3) == 1 and s.count(2) == 1 and s.count(1) == 1:
        print(0)
    elif s.count(4) == 1 and s.count(3) == 1 and s.count(2) == 1:
        print(1)
    elif s.count(4) == 1 and s.count(3) == 1 and s.count(1) == 1:
        print(1)
    elif s.count(4) == 1 and s.count(2) == 1 and s.count(1) == 1:
        print(1)
    elif s.count(3) == 1 and s.count(2) == 1 and s.count(1) == 1:
        print(1)
    elif s.count(4) == 1 and s.count(3) == 1:
        print(2)
    elif s.count(4) == 1 and s.count(2) == 1:
        print(2)
    elif s.count(4) == 1 and s.count(1) == 1:
        print(2)
    elif s.count(3) == 1 and s.count(2) == 1:
        print(2)
    elif s.count(3) == 1 and s.count(1) == 1:
        print(2)
    elif s.count(2) == 1 and s.count(1) == 1:
        print(2)
    elif s.count(4) == 1:
        print(3)
    elif s.count(3) == 1:
        print(3)
    elif s.count(2) == 1:
        print(3)
    elif s.count(1) == 1:
        print(3)
    else:
        print(4)
