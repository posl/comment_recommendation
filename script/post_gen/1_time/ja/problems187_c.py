Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = set()
    for i in range(N):
        s = input()
        if s[0] == '!':
            if s[1:] in S:
                print(s[1:])
                return
            else:
                S.add(s)
        else:
            if '!' + s in S:
                print(s)
                return
            else:
                S.add(s)
    print('satisfiable')

main()

=======
Suggestion 2

def main():
    N = int(input())
    S = set()
    for i in range(N):
        s = input()
        if s[0] == '!':
            if s[1:] in S:
                print(s[1:])
                exit()
            else:
                S.add(s)
        else:
            if '!' + s in S:
                print(s)
                exit()
            else:
                S.add(s)
    print('satisfiable')

=======
Suggestion 3

def main():
    N = int(input())
    S = set()
    for _ in range(N):
        s = input()
        if s[0] == '!':
            if s[1:] in S:
                print(s[1:])
                return
        else:
            if '!' + s in S:
                print(s)
                return
        S.add(s)
    print('satisfiable')

=======
Suggestion 4

def main():
    n = int(input())
    s = set()
    for i in range(n):
        s.add(input())
    for i in s:
        if '!' + i in s:
            print(i)
            exit()
    print('satisfiable')

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if "!" + s in S:
            print(s)
            return
    print("satisfiable")

=======
Suggestion 6

def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    for i in range(n):
        if s[i][0] == "!":
            s[i] = s[i][1:]
    s.sort()
    for i in range(n-1):
        if s[i] == s[i+1]:
            print(s[i])
            exit()
    print("satisfiable")

=======
Suggestion 7

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S = set(S)
    for i in S:
        if "!" + i in S:
            print(i)
            exit()
    print("satisfiable")

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == '!':
            S1.add(s[1:])
        else:
            S2.add(s)
    S3 = S1 & S2
    if len(S3) > 0:
        print(list(S3)[0])
    else:
        print('satisfiable')

=======
Suggestion 9

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i][0] == '!':
            continue
        if S[i][1:] == S[i+1][1:]:
            print(S[i][1:])
            exit()
    print('satisfiable')

=======
Suggestion 10

def resolve():
    from collections import defaultdict
    n = int(input())
    d = defaultdict(int)
    for i in range(n):
        s = input()
        d[s] += 1

    for k, v in d.items():
        if k[0] == "!":
            if d[k[1:]] > 0:
                print(k[1:])
                exit()
        else:
            if d["!" + k] > 0:
                print(k)
                exit()
    print("satisfiable")
