Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a = [i-1 for i in a]
    #print(a)
    #print(x)
    #print(n)
    #ans = 0
    #for i in range(n):
    #    if x == i+1:
    #        continue
    #    if a[i] == x:
    #        ans += 1
    #        continue
    #    if a[a[i]] == x:
    #        ans += 1
    #print(ans)
    #print(a)
    #print(x)
    #print(n)
    #print(a[x-1])
    #print(a[a[x-1]])
    #print(a[a[a[x-1]]])
    #print(a[a[a[a[x-1]]]])
    #print(a[a[a[a[a[x-1]]]]])
    #print(a[a[a[a[a[a[x-1]]]]]])
    #print(a[a[a[a[a[a[a[x-1]]]]]]])
    #print(a[a[a[a[a[a[a[a[x-1]]]]]]]])
    #print(a[a[a[a[a[a[a[a[a[x-1]]]]]]]]])
    #print(a[a[a[a[a[a[a[a[a[a[x-1]]]]]

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = -1
    count = 1
    for i in range(n):
        if a[i] == -1:
            continue
        else:
            while True:
                if a[i] == -1:
                    break
                else:
                    i = a[i] - 1
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    ans = 1
    for i in range(n):
        if a[i] == 0:
            continue
        else:
            ans += 1
            a[a[i]-1] = 0
    print(ans)

=======
Suggestion 4

def main():
    # 標準入力の取得
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    # 処理
    # 入力値のうち、x番目の値を取得
    target = a[x-1]
    # 結果の初期化
    result = 1
    # 取得した値がx番目の値と同じでない限り処理を繰り返す
    while target != x:
        # 結果に+1する
        result += 1
        # 取得した値を更新する
        target = a[target-1]
    # 結果の出力
    print(result)
    return

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [i-1 for i in a]

    known = [False] * n
    known[x-1] = True
    cnt = 1
    for i in range(n):
        if known[a[i]]:
            cnt += 1
            known[i] = True
    print(cnt)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, 0)
    a.insert(0, 0)
    count = 0
    for i in range(1, n+1):
        if a[i] == x:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    a[x-1] = 0
    ans = 1
    for i in range(n):
        if a[i] != 0:
            ans += 1
            a[a[i]-1] = 0
    print(ans)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a
    count = 0
    for i in range(1, n + 1):
        if a[i] == x:
            count += 1
            x = i
    print(count)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    ans = 1
    tmp = X
    while True:
        if tmp == A[tmp]:
            break
        tmp = A[tmp]
        ans += 1
    print(ans)

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a[x-1] = 0
    ans = 1
    for i in a:
        if i != 0:
            ans += 1
    print(ans)
