Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    for i in range(n):
        if '!' + s[i] in s:
            print(s[i])
            return
    print('satisfiable')

=======
Suggestion 2

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print(s[i])
            return
        elif s[i] == s[i+1][1:]:
            print(s[i+1])
            return
    print('satisfiable')

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    s = set()
    for i in range(N):
        if S[i][0] == "!":
            if S[i][1:] in s:
                print(S[i][1:])
                return
        else:
            if "!" + S[i] in s:
                print(S[i])
                return
        s.add(S[i])
    print("satisfiable")

=======
Suggestion 4

def main():
    n = int(input())
    s = [input() for i in range(n)]
    s1 = []
    s2 = []
    for i in s:
        if i[0] == "!":
            s1.append(i[1:])
        else:
            s2.append(i)
    s1 = set(s1)
    s2 = set(s2)
    s3 = s1 & s2
    if len(s3) == 0:
        print("satisfiable")
    else:
        print(s3.pop())

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    for i in range(N-1):
        if S[i][0] == '!':
            if S[i][1:] == S[i+1]:
                print(S[i][1:])
                return
    print('satisfiable')

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    s.sort()
    i = 0
    while i < n-1:
        if s[i] == s[i+1]:
            i += 2
        elif s[i] == '!'+s[i+1]:
            print(s[i][1:])
            return
        else:
            i += 1
    print('satisfiable')

=======
Suggestion 7

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s1 = [i[1:] for i in s if i[0] == '!']
    s2 = [i for i in s if i[0] != '!']
    for i in s1:
        if i in s2:
            print(i)
            return
    print('satisfiable')

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.reverse()
    for s in S:
        if '!' + s in S:
            print(s)
            return
    print('satisfiable')
    return

=======
Suggestion 9

def main():
    #input
    N = int(input())
    S = [input() for _ in range(N)]

    #create a dictionary
    D = {}
    for s in S:
        if s[0] == '!':
            D[s[1:]] = 1
        else:
            D[s] = 0

    #output
    for s in S:
        if s[0] == '!':
            if D[s[1:]] == 0:
                print(s[1:])
                return
        else:
            if D[s] == 1:
                print(s)
                return
    print('satisfiable')

=======
Suggestion 10

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    #print(N)
    #print(S)
    for i in range(N):
        if S[i][0] == '!':
            S[i] = S[i][1:]
            if S[i] in S:
                print(S[i])
                break
        else:
            if '!' + S[i] in S:
                print(S[i])
                break
    else:
        print('satisfiable')
