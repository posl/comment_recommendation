Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i] == S[i+1]:
            print(S[i])
            return
        elif S[i][1:] == S[i+1]:
            print(S[i][1:])
            return
    print("satisfiable")

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    for i in range(N-1):
        if S[i] == S[i+1]:
            print(S[i])
            return
        if S[i][1:] == S[i+1]:
            print(S[i][1:])
            return
    print('satisfiable')

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for i in range(N)]
    for i in range(N):
        if S[i][0] == "!":
            if S[i][1:] in S:
                print(S[i][1:])
                return
        else:
            if "!" + S[i] in S:
                print(S[i])
                return
    print("satisfiable")
    return

=======
Suggestion 4

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    S.sort()
    for i in range(N-1):
        if S[i] == S[i+1]:
            print(S[i])
            return
        if S[i] == "!" + S[i+1]:
            print(S[i+1])
            return
    print("satisfiable")

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == "!":
            S1.add(s)
        else:
            S2.add(s)
    for s in S1:
        if s[1:] in S2:
            print(s[1:])
            return
    print("satisfiable")

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = [s[1:] for s in S if s.startswith("!")]
    S2 = [s for s in S if not s.startswith("!")]
    S1 = set(S1)
    S2 = set(S2)
    for s in S1:
        if s in S2:
            print(s)
            return
    print("satisfiable")

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == "!":
            S1.add(s[1:])
        else:
            S2.add(s)

    ans = S1 & S2
    if ans:
        print(list(ans)[0])
    else:
        print("satisfiable")

main()

=======
Suggestion 8

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S = list(set(S))
    for s in S:
        if '!' + s in S:
            print(s)
            return
    print('satisfiable')
    return

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = sorted(S)
    for i in range(N-1):
        if S[i][0] == '!':
            if S[i+1][0] != '!':
                if S[i][1:] == S[i+1]:
                    print(S[i][1:])
                    return
    print('satisfiable')

=======
Suggestion 10

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S1 = set(S)
    S2 = set([s[1:] if s[0] == "!" else "!" + s for s in S])
    if len(S1 & S2) > 0:
        print((S1 & S2).pop())
    else:
        print("satisfiable")
