Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    for s in sorted(S, key=lambda s: [X.index(c) for c in s]):
        print(s)

=======
Suggestion 2

def main():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    S.sort(key=lambda s: [X.index(c) for c in s])
    for s in S:
        print(s)

=======
Suggestion 3

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    print(*sorted(S, key=lambda s: [X.index(c) for c in s]), sep='

')

=======
Suggestion 4

def main():
    X = input()
    N = int(input())
    S = [input() for i in range(N)]
    S.sort(key=lambda x: [X.index(c) for c in x])
    for s in S:
        print(s)

=======
Suggestion 5

def main():
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())

    for i in range(N):
        for j in range(N-1):
            if S[j] > S[j+1]:
                S[j], S[j+1] = S[j+1], S[j]
            elif S[j] == S[j+1]:
                continue
            else:
                for k in range(len(S[j])):
                    if X.index(S[j][k]) > X.index(S[j+1][k]):
                        S[j], S[j+1] = S[j+1], S[j]
                        break
                    elif X.index(S[j][k]) == X.index(S[j+1][k]):
                        continue
                    else:
                        break

    for i in range(N):
        print(S[i])

=======
Suggestion 6

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    dic = {X[i]: i for i in range(26)}
    S.sort(key=lambda x: [dic[x[i]] for i in range(len(x))])
    for s in S:
        print(s)

=======
Suggestion 7

def main():
    X = list(input())
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort(key = lambda x: [X.index(c) for c in x])
    for s in S:
        print(s)

=======
Suggestion 8

def main():
    #入力
    X = input()
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    #辞書順にソート
    S.sort(key=lambda x: [X.index(i) for i in x])
    #出力
    for i in range(N):
        print(S[i])

=======
Suggestion 9

def main():
    import sys
    input = sys.stdin.readline
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    # 文字列を辞書順に並べ替える
    X = {X[i]: i for i in range(26)}
    S.sort(key=lambda x: [X[c] for c in x])
    for s in S:
        print(s, end="")

=======
Suggestion 10

def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]

    # Xの順番を辞書にしておく
    # X = "zyxwvutsrqponmlkjihgfedcba"
    # X_dict = {"z":0, "y":1, "x":2, ...}
    X_dict = {X[i]:i for i in range(len(X))}

    # Sの文字列をXの順番で並べ替える
    # S = ["a", "ab", "abc", "ac", "b"]
    # S_sort = ["a", "ac", "ab", "abc", "b"]
    S_sort = sorted(S, key=lambda x: [X_dict[s] for s in x])

    # 並べ替えたSを出力
    for s in S_sort:
        print(s)
