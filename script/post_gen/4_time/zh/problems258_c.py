Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, q = map(int, input().split())
    s = input()
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])

=======
Suggestion 2

def solve():
    n, q = map(int, input().split())
    s = input()
    for _ in range(q):
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
    query = [list(map(int, input().split())) for _ in range(Q)]

    for t, x in query:
        if t == 1:
            S = S[N-x:] + S[:N-x]
        else:
            print(S[x-1])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    S = input()
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            S = S[N-x:] + S[:N-x]
        else:
            print(S[x-1])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    S = input()
    queries = [list(map(int, input().split())) for _ in range(Q)]


    # S = list(S)
    # for q in queries:
    #     if q[0] == 1:
    #         for _ in range(q[1]):
    #             S.insert(0, S.pop())
    #     else:
    #         print(S[q[1]-1])

    S = S*2
    for q in queries:
        if q[0] == 1:
            S = S[N-q[1]:2*N-q[1]]
        else:
            print(S[q[1]-1])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    S = input()
    query = [list(map(str, input().split())) for _ in range(Q)]
    for i in range(Q):
        if query[i][0] == '1':
            S = S[-1] + S[:-1]
        else:
            print(S[int(query[i][1])-1])

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    S = input()

    # 1-indexedにする
    S = " " + S

    # 累積和
    cum = [0] * (N + 1)
    for i in range(1, N + 1):
        cum[i] = cum[i - 1] + ord(S[i]) - ord("a") + 1

    #print(cum)

    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            cum[x] = cum[x] - ord(S[x]) + ord(S[x - 1])
            cum[x - 1] = cum[x - 1] - ord(S[x - 1]) + ord(S[x])
            S = S[:x - 1] + S[x] + S[x - 1] + S[x + 1:]
        else:
            print(cum[x] - cum[x - 1])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    S = input()
    for i in range(Q):
        t, x = map(str, input().split())
        if t == '2':
            print(S[int(x) - 1])
        else:
            S = S[-1] + S[:-1]
    return 0

=======
Suggestion 9

def main():
    n, q = map(int, input().split())
    s = list(input())
    for i in range(q):
        t, x = map(int, input().split())
        if t == 1:
            s = s[-x:] + s[:-x]
        else:
            print(s[x-1])
