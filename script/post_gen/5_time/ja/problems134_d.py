Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    a = list(map(int, input().split()))
    b = [0] * N
    for i in range(N, 0, -1):
        sum = 0
        for j in range(i, N+1, i):
            sum += b[j-1]
        if sum % 2 != a[i-1]:
            b[i-1] = 1
    M = sum(b)
    print(M)
    if M > 0:
        for i in range(N):
            if b[i] == 1:
                print(i+1, end=" ")
        print()

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n - 1, -1, -1):
        if sum(b[i::i+1]) % 2 != a[i]:
            b[i] = 1
    print(sum(b))
    if sum(b) > 0:
        print(*[i+1 for i in range(n) if b[i] == 1])

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))

    b = [0] * n
    for i in reversed(range(1, n + 1)):
        s = sum(b[i - 1::i]) % 2
        if s != a[i - 1]:
            b[i - 1] = 1
    m = sum(b)
    if m == 0:
        print(0)
    else:
        print(m)
        print(*[i + 1 for i, j in enumerate(b) if j == 1])

=======
Suggestion 4

def main():
    N = int(input())
    a = list(map(int, input().split()))
    if N == 1:
        if a[0] == 0:
            print(1)
            print(1)
        else:
            print(-1)
        return
    if N == 2:
        if a[0] == 0 and a[1] == 0:
            print(2)
            print("1 2")
        elif a[0] == 1 and a[1] == 1:
            print(2)
            print("1 2")
        elif a[0] == 0 and a[1] == 1:
            print(2)
            print("1 2")
        elif a[0] == 1 and a[1] == 0:
            print(2)
            print("1 2")
        else:
            print(-1)
        return
    if a[0] == 1:
        print(-1)
        return
    if a[1] == 1:
        print(-1)
        return
    if a[0] == 0 and a[1] == 0:
        print(2)
        print("1 2")
        return
    if a[0] == 0 and a[1] == 1:
        print(-1)
        return
    if a[0] == 1 and a[1] == 0:
        print(-1)
        return
    if a[0] == 1 and a[1] == 1:
        print(-1)
        return
    print(N)
    for i in range(1, N+1):
        print(i)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(n, 0, -1):
        c = 0
        for j in range(i, n + 1, i):
            c += b[j - 1]
        if c % 2 != a[i - 1]:
            b.append(1)
        else:
            b.append(0)
    print(sum(b))
    for k in range(len(b)):
        if b[k] == 1:
            print(k + 1, end=' ')
    print()

=======
Suggestion 6

def main():
    N = int(input())
    a = [int(i) for i in input().split()]
    b = [0] * (N+1)
    for i in range(N, 0, -1):
        if a[i-1] != sum(b[i::i]) % 2:
            b[i] = 1
    print(sum(b))
    if sum(b) > 0:
        print(*[i for i, x in enumerate(b) if x == 1])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0]*N
    for i in range(N-1, -1, -1):
        #print(i)
        #print(B)
        cnt = 0
        for j in range(i+1, N+1, i+1):
            #print(j)
            cnt += B[j-1]
        #print(cnt)
        if cnt % 2 != A[i]:
            B[i] = 1
    ans = []
    for i in range(N):
        if B[i] == 1:
            ans.append(i+1)
    print(len(ans))
    if len(ans) > 0:
        print(*ans)

=======
Suggestion 8

def main():
    # データ入力
    N = int(input())
    a = list(map(int, input().split()))

    # 処理
    # 一番後ろから処理していく
    # 1が書かれた箱にボールを入れるか入れないかを決める
    # 1が書かれた箱にボールを入れた場合、その箱の倍数にあたる箱にはボールを入れない
    # 1が書かれた箱にボールを入れなかった場合、その箱の倍数にあたる箱にはボールを入れる
    # 1が書かれた箱にボールを入れるか入れないかは、その箱の倍数にあたる箱に入れるボールの個数の和の偶奇で決まる
    # 1が書かれた箱にボールを入れる場合、その箱の倍数にあたる箱にはボールを入れない
    # 1が書かれた箱にボールを入れない場合、その箱の倍数にあたる箱にはボールを入れる
    # 1が書かれた箱にボールを入れるか入れないかは、その箱の倍数にあたる箱に入れるボールの個数の和の偶奇で決まる
    # 1が書かれた箱にボールを入れる場合、その箱の倍数にあたる箱にはボールを入れない
    # 1が書かれた箱にボールを入れない場合、その箱の倍数にあたる箱にはボールを入れる
    # 1が書かれた箱にボールを入れるか入れないかは、その箱の倍数にあたる箱に

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    for i in range(N):
        if A[i] == 1:
            for j in range(i+1, N):
                if (j+1) % (i+1) == 0:
                    A[j] = (A[j] + 1) % 2
    print(sum(A))
    for i in range(N):
        if A[i] == 1:
            print(i+1)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n, 0, -1):
        if a[i-1] == 1:
            ans.append(i)
            for j in range(i-1, 0, -1):
                if j % i == 0:
                    if a[j-1] == 1:
                        a[j-1] = 0
                    else:
                        a[j-1] = 1
    print(len(ans))
    if len(ans) != 0:
        print(*ans)
