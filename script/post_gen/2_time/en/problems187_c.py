Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    s = set()
    for i in range(n):
        si = input()
        if si[0] == "!":
            if si[1:] in s:
                print(si[1:])
                return
            else:
                s.add(si)
        else:
            if "!" + si in s:
                print(si)
                return
            else:
                s.add(si)
    print("satisfiable")

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    for i in range(N):
        if "!" + S[i] in S:
            print(S[i])
            return
    print("satisfiable")
    return

=======
Suggestion 3

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = set(S)
    for s in S:
        if '!' + s in S:
            print(s)
            return
    print('satisfiable')

=======
Suggestion 4

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
    S3 = S1 & S2
    if len(S3) == 0:
        print("satisfiable")
    else:
        print(S3.pop())

=======
Suggestion 5

def main():
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i] == "!" + S[i+1]:
            print(S[i+1])
            return
    print("satisfiable")

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S_set = set(S)

    for s in S:
        if '!' + s in S_set:
            print(s)
            return

    print('satisfiable')

=======
Suggestion 7

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S = [s[1:] if s[0] == '!' else s for s in S]
    if len(S) != len(set(S)):
        print([s for s in S if S.count(s) > 1][0])
    else:
        print('satisfiable')

=======
Suggestion 8

def main():
    N = int(input())
    s = [input() for _ in range(N)]
    d = {}
    for i in range(N):
        if s[i][0] == '!':
            s[i] = s[i][1:]
            d[s[i]] = 1
        else:
            d[s[i]] = 0
    for i in range(N):
        if d[s[i]] == 1:
            print(s[i])
            return
    print('satisfiable')
    return

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    S.append('')

    for i in range(N):
        if S[i][0] == '!':
            if S[i] == S[i+1]:
                print(S[i][1:])
                return

    print('satisfiable')

=======
Suggestion 10

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    # !aとaのペアを作成する
    # その際、aが存在しない場合は空文字列を代入する
    S_pair = {}
    for s in S:
        if s[0] == "!":
            S_pair[s[1:]] = s
        else:
            S_pair[s] = ""

    # S_pairの中で、空文字列を持つキーを探す
    for k, v in S_pair.items():
        if v == "":
            continue
        else:
            if k in S_pair:
                print(k)
                return

    print("satisfiable")
