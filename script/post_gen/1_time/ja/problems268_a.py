Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B, C, D, E = map(int, input().split())
    print(len(set([A, B, C, D, E])))

=======
Suggestion 2

def main():
    # A, B, C, D, E = map(int, input().split())
    # print(len(set([A, B, C, D, E])))
    print(len(set(input().split())))

=======
Suggestion 3

def main():
    # input
    As = [*map(int, input().split())]

    # compute
    As = set(As)

    # output
    print(len(As))

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    print(len(set(a)))

=======
Suggestion 5

def main():
    #入力
    A, B, C, D, E = map(int, input().split())
    #print(A, B, C, D, E)
    #リストに値を格納
    L = [A, B, C, D, E]
    #print(L)
    #リストの要素の個数を出力
    print(len(set(L)))

=======
Suggestion 6

def main():
    #入力
    A = list(map(int,input().split()))
    #出力
    print(len(set(A)))
