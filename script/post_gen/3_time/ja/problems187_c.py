Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S1 = [s[1:] for s in S if s[0] == "!"]
    S2 = [s for s in S if s[0] != "!"]
    S1.sort()
    S2.sort()
    for i in range(N-1):
        if S1[i] == S2[i]:
            print(S1[i])
            return
    print("satisfiable")

=======
Suggestion 2

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    for i in range(N-1):
        if S[i][0] == "!":
            if S[i][1:] == S[i+1]:
                print(S[i][1:])
                return
    print("satisfiable")
    return

=======
Suggestion 3

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

    for s in S2:
        if "!" + s in S1:
            print(s)
            return

    print("satisfiable")

=======
Suggestion 4

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S1 = set()
    S2 = set()
    for s in S:
        if s[0] == '!':
            S2.add(s[1:])
        else:
            S1.add(s)
    for s in S1:
        if s in S2:
            print(s)
            return
    print('satisfiable')

=======
Suggestion 5

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    s1 = [i for i in s if i[0] != '!']
    s2 = [i[1:] for i in s if i[0] == '!']
    s1 = set(s1)
    s2 = set(s2)
    for i in s1:
        if i in s2:
            print(i)
            return
    print('satisfiable')

=======
Suggestion 6

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    sn = set(s)
    for i in sn:
        if i[0] == "!":
            if i[1:] in sn:
                print(i[1:])
                return
    print("satisfiable")

=======
Suggestion 7

def main():
    #入力
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()

    #処理
    for i in range(N-1):
        if S[i][0] == "!":
            if S[i][1:] == S[i+1]:
                print(S[i][1:])
                return

    print("satisfiable")

=======
Suggestion 8

def main():
    # 入力
    N = int(input())
    S = [input() for _ in range(N)]

    # 処理
    S = set(S)
    for s in S:
        if '!' + s in S:
            print(s)
            exit()

    # 出力
    print('satisfiable')

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    #重複を除く
    S = list(set(S))

    #先頭に ! が付いているかどうかで、リストを分ける
    S_with_exclamation = [s for s in S if s[0] == "!"]
    S_without_exclamation = [s for s in S if s[0] != "!"]

    #先頭に ! が付いているものと付いていないものの重複を取り除いているので、
    #重複があれば不満な文字列が存在する
    for s in S_with_exclamation:
        if s[1:] in S_without_exclamation:
            print(s[1:])
            return

    print("satisfiable")
    return
