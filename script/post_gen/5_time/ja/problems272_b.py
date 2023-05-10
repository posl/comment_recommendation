Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    k = []
    x = []
    for i in range(m):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    for i in range(m):
        for j in range(i+1, m):
            if len(set(x[i]) & set(x[j])) >= 2:
                print("Yes")
                return
    print("No")

=======
Suggestion 2

def check(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                return True
    return False

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    for j in range(i + 1, m):
        if check(a[i], a[j]):
            print("Yes")
            exit()
print("No")

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(m)]

    for i in range(m):
        a[i].pop(0)

    for i in range(m):
        for j in range(i+1,m):
            if len(set(a[i]) & set(a[j])) > 0:
                print("Yes")
                exit()
    print("No")

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    # N 人の人がいます。
    # M 回の舞踏会が行われました。
    # i (1≦ i ≦ M) 回目の舞踏会には k_i 人が参加し、
    # 参加した人は人 x_{i,1},x_{i,2},...,x_{i,k_i} でした。
    # どの二人も少なくとも 1 回同じ舞踏会に参加したか判定してください。
    # 2≦ N ≦ 100
    # 1≦ M ≦ 100
    # 2≦ k_i ≦ N
    # 1≦ x_{i,1}<x_{i,2}<... < x_{i,k_i}≦ N
    # 入力は全て整数
    # 入力は以下の形式で標準入力から与えられる。
    # N M
    # k_1 x_{1,1} x_{1,2} ... x_{1,k_1}
    # .
    # .
    # .
    # k_M x_{M,1} x_{M,2} ... x_{M,k_M}
    # どの二人も少なくとも 1 回同じ舞踏会に参加した場合 Yes を、そうでない場合 No を出力せよ。
    # 人 1 と人 2 は共に 1 回目の舞踏会に参加しています。
    # 人 2 と人 3 は共に 2 回目の舞踏会に参加しています。
    # 人 1 と人 3 は共に 3 回目の舞踏会に参加しています。
    # 以上よりどの二人も少なくとも 1 回同じ舞踏会に参加したので、答えは Yes です。
    #

=======
Suggestion 5

def main():
    n,m = map(int, input().split())
    a = []
    for i in range(m):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(i+1,n):
            if not (i+1 in a[j-1]):
                print("No")
                return
    print("Yes")

=======
Suggestion 6

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split()))[1:] for _ in range(M)]

    for i in range(N):
        for j in range(i+1, N):
            for k in range(M):
                if i+1 not in A[k] or j+1 not in A[k]:
                    break
            else:
                print("No")
                return
    print("Yes")

=======
Suggestion 7

def main():
    N, M = map(int, input().split())
    k = []
    x = []
    for i in range(M):
        k.append(list(map(int, input().split())))
        x.append(k[i][1:])
    for i in range(N):
        for j in range(N):
            if i != j:
                if set(x[i]) & set(x[j]):
                    print('Yes')
                    return
    print('No')

=======
Suggestion 8

def main():
    n,m = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(m)]
    b = []
    for i in range(m):
        for j in range(1,a[i][0]+1):
            b.append(a[i][j])
    c = list(set(b))
    if len(c) == len(b):
        print('No')
    else:
        print('Yes')

=======
Suggestion 9

def main():
    N, M = map(int, input().split())
    X = []
    for i in range(M):
        X.append(list(map(int, input().split()))[1:])
    for i in range(M):
        for j in range(i+1, M):
            if len(set(X[i]) & set(X[j])) != 0:
                print("Yes")
                return
    print("No")

=======
Suggestion 10

def main():
    n, m = map(int, input().split())

    p = [0] * n
    for _ in range(m):
        k, *x = map(int, input().split())
        for i in x:
            p[i - 1] += 1

    for i in p:
        if i == 0:
            print('No')
            return
    print('Yes')
