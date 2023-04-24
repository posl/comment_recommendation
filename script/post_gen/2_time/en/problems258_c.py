Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[-x:] + S[:-x]
        else:
            print(S[x-1])

=======
Suggestion 2

def main():
    n, q = map(int, input().split())
    s = input()
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x - 1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    S = input()
    S = S[::-1]
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[1:] + S[0]
        else:
            print(S[N-x])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    queries = [list(map(int, input().split())) for _ in range(Q)]
    print(N, Q)
    print(S)
    print(queries)

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    S = input()
    queries = [list(map(int, input().split())) for _ in range(Q)]
    ans = []
    for t, x in queries:
        if t == 1:
            S = S[-x:] + S[:-x]
        else:
            ans.append(S[x-1])
    print(''.join(ans))

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    query = []
    for i in range(Q):
        query.append(list(map(str, input().split())))

    #print(N, Q)
    #print(S)
    #print(query)

    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])
    #print(S[4])
    #print(S[5])
    #print(S[6])
    #print(S[7])
    #print(S[8])
    #print(S[9])

    #print(N, Q)
    #print(S)
    #print(query)

    for i in range(Q):
        if query[i][0] == '1':
            S = S[N-1] + S[0:N-1]
            #print(S)
        else:
            print(S[int(query[i][1])-1])

=======
Suggestion 7

def main():
    n, q = map(int, input().split())
    s = input()
    queries = [list(map(int, input().split())) for _ in range(q)]
    s = list(s)
    for i in range(q):
        if queries[i][0] == 1:
            s.insert(0, s.pop())
        else:
            print(s[queries[i][1]-1])
    return

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = input()
    queries = [list(map(int, input().split())) for _ in range(Q)]
    #print(queries)
    #print(S)
    #print(N, Q)
    #print(S)
    #print(queries)

    for query in queries:
        if query[0] == 1:
            S = S[-1] + S[:-1]
        else:
            print(S[query[1]-1])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    S = input()
    query = [list(map(int, input().split())) for _ in range(Q)]

    # 先頭の文字を基準にして、その文字の位置を記録しておく
    # その文字を削除したときに、その文字の位置がどこに移動するかを計算する
    # その文字の位置を計算するために、文字の出現回数を記録しておく
    # あとは、文字の出現回数を利用して、文字の位置を計算する
    # ただし、文字の出現回数は、文字の位置を計算するために利用するため、
    # 一度計算したら、その値を利用する
    # そのために、文字の出現回数を記録する辞書を用意する
    # この辞書は、文字の出現回数を記録するためのものであり、
    # あくまで文字の出現回数を記録するためのものであり、
    # 文字の位置を計算するために利用するためのものではない
    # 文字の位置を計算するために利用するためのものは、新たに用意する
    # 文字の位置を計算するために利用する辞書は、
    # 文字の出現回数を記録する辞書とは異なる辞書とする
    # 文字の位置を計算するために利用する辞書は、
    # 文字の出現回数を記録する辞書を利用して、
    # 文字の位置を計算する
    # この計算は、文字の出現回数を記録する辞書が更新されるたびに、
    # 文字の位置を

=======
Suggestion 10

def read_int():
    return int(input())
