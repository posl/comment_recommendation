Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

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
Suggestion 3

def main():
    n, m = map(int, input().split())
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
    n, m = map(int, input().split())
    s = list(map(str, input().split()))
    t = list(map(str, input().split()))
    for i in range(n):
        if s[i] in t:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    s = input().split()
    t = input().split()
    for i in range(n):
        if s[i] in t:
            print('Yes')
        else:
            print('No')
    return

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    for i in range(1, N + 1):
        if S[i - 1] in T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    #入力
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    
    #急行列車が止まる駅のリスト
    stop = []
    
    #急行列車が止まる駅のリストを作成
    for i in range(M):
        stop.append(T[i])
    
    #各駅に急行列車が止まるかどうか判定
    for i in range(N):
        if S[i] in stop:
            print("Yes")
        else:
            print("No")

=======
Suggestion 8

def main():
    #N, M = map(int, input().split())
    #S = list(map(str, input().split()))
    #T = list(map(str, input().split()))
    N, M = 5, 3
    S = ['tokyo', 'kanda', 'akiba', 'okachi', 'ueno']
    T = ['tokyo', 'akiba', 'ueno']
    for i in range(N):
        if S[i] in T:
            print('Yes')
        else:
            print('No')

=======
Suggestion 9

def main():
    #入力
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    #処理
    for i in range(N):
        if S[i] in T:
            print("Yes")
        else:
            print("No")
    #出力

=======
Suggestion 10

def main():
    N, M = map(int, input().split())
    S = input().split()
    T = input().split()
    i = 0
    j = 0
    for i in range(N):
        if S[i] == T[j]:
            print("Yes")
            j += 1
        else:
            print("No")
        if j == M:
            break
    for i in range(i + 1, N):
        print("No")
