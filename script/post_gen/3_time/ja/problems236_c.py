Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 2

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    for i in range(N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    S = set(input().split())
    T = set(input().split())
    for i in range(1, N+1):
        if S[i-1] in T:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    set_T = set(T)
    for s in S:
        if s in set_T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    #print(N, M)
    #print(S)
    #print(T)
    #急行列車が止まる駅のリストを作成
    stop = []
    for i in range(M):
        stop.append(T[i])
    #print(stop)
    #急行列車が止まるかどうか判定
    for i in range(N):
        if S[i] in stop:
            print("Yes")
        else:
            print("No")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    # print(N, M)
    # print(S)
    # print(T)

    # 急行列車が止まる駅を集める
    stops = []
    for i in range(M):
        # print(T[i])
        for j in range(N):
            # print(S[j])
            if T[i] == S[j]:
                stops.append(j)
    # print(stops)

    # 駅の一覧を出力
    for i in range(N):
        if i in stops:
            print('Yes')
        else:
            print('No')
