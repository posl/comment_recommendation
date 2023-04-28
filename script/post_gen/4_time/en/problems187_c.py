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
        elif S[i] == "!" + S[i+1]:
            print(S[i+1])
            return
    print("satisfiable")
    return

main()

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    T = set()
    for s in S:
        if s[0] == "!":
            T.add(s[1:])
        else:
            T.add(s)
    for t in T:
        if "!" + t in T:
            print(t)
            return
    print("satisfiable")
    return

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = set()
    for i in range(n):
        if s[i][0] == "!":
            if s[i][1:] in t:
                print(s[i][1:])
                return
        else:
            if "!" + s[i] in t:
                print(s[i])
                return
        t.add(s[i])
    print("satisfiable")

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if s[0] == "!":
            if s[1:] in S:
                print(s[1:])
                return
    print("satisfiable")
    return

main()

=======
Suggestion 5

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if s[0] == "!":
            if s[1:] in S:
                print(s[1:])
                return
        else:
            if "!" + s in S:
                print(s)
                return
    print("satisfiable")
    return

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]
    dic = {}
    for i in range(N):
        if S[i][0] == "!":
            if S[i][1:] in dic:
                print(S[i][1:])
                return
            else:
                dic[S[i][1:]] = 1
        else:
            if "!"+S[i] in dic:
                print(S[i])
                return
            else:
                dic[S[i]] = 1
    print("satisfiable")
    return

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    for i in range(N-1):
        if S[i][0] == "!":
            if S[i+1][0] != "!":
                if S[i][1:] == S[i+1]:
                    print(S[i][1:])
                    return
            else:
                if S[i][1:] == S[i+1][1:]:
                    print(S[i][1:])
                    return
    print("satisfiable")
    return

=======
Suggestion 8

def main():
    N = int(input())
    words = []
    for i in range(N):
        words.append(input())
    words.sort()
    for i in range(N-1):
        if words[i] == "!" + words[i+1]:
            print(words[i+1])
            return
    print("satisfiable")

main()

=======
Suggestion 9

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s = set(s)

    for i in s:
        if i[0] == "!":
            if i[1:] in s:
                print(i[1:])
                return
        else:
            if "!" + i in s:
                print(i)
                return

    print("satisfiable")

=======
Suggestion 10

def main():

    #入力
    N = int(input())
    S = [input() for _ in range(N)]

    #重複を削除
    S = list(set(S))

    #出力
    for i in range(len(S)):
        if "!" + S[i] in S:
            print(S[i])
            exit()

    print("satisfiable")
