Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s - 1][t])

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    B = [list(map(int, input().split())) for i in range(Q)]
    for i in range(Q):
        print(A[B[i][0] - 1][B[i][1] - 1])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        a = list(map(int, input().split()))
        A.append(a)
    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t])

=======
Suggestion 5

def main():
    N, Q = map(int, input().split())
    L = []
    for i in range(N):
        L.append(list(map(int, input().split())))
    S = []
    T = []
    for i in range(Q):
        s, t = map(int, input().split())
        S.append(s)
        T.append(t)
    for i in range(Q):
        print(L[S[i] - 1][T[i]])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    L = [list(map(int, input().split())) for _ in range(N)]
    S, T = zip(*[map(int, input().split()) for _ in range(Q)])
    for s, t in zip(S, T):
        print(L[s-1][t])

=======
Suggestion 7

def solve():
    N, Q = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s - 1][t])

=======
Suggestion 8

def main():
    #入力
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        L = list(map(int, input().split()))
        A.append(L)
    #print(A)
    B = []
    for i in range(Q):
        s, t = map(int, input().split())
        B.append(s)
        B.append(t)
    #print(B)
    for i in range(Q):
        print(A[B[2*i]-1][B[2*i+1]])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    #N, Q = 3, 4
    #L = [4, 2, 3]
    #A = [[128, 741, 239, 901], [1, 1], [314, 159, 26535]]
    L = []
    A = []
    for i in range(N):
        l = list(map(int, input().split()))
        #l = A[i]
        L.append(l[0])
        A.append(l[1:])
    #print(L)
    #print(A)
    #print(N, Q)
    #print(A)
    #print(L)
    for i in range(Q):
        s, t = map(int, input().split())
        #s, t = A[i + N]
        print(A[s - 1][t - 1])
    #print(A)
main()

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    #数列の長さの配列
    L = []
    #数列の配列
    A = []
    for i in range(N):
        L.append(list(map(int, input().split())))
        A.append(L[i][1:])
    
    #クエリの配列
    S = []
    T = []
    for i in range(Q):
        S.append(list(map(int, input().split())))
        T.append(S[i][1])
    
    #Sの配列の要素をAの要素に変換
    for i in range(Q):
        print(A[S[i][0]-1][T[i]-1])
