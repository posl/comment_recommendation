Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        for j in range(B[i]+1):
            if A[i]*j == X:
                print("Yes")
                return
            elif A[i]*j > X:
                break
            else:
                X = X - A[i]*j
                for k in range(N):
                    for l in range(B[k]+1):
                        if A[k]*l == X:
                            print("Yes")
                            return
                        elif A[k]*l > X:
                            break
                        else:
                            X = X - A[k]*l
                            for m in range(N):
                                for n in range(B[m]+1):
                                    if A[m]*n == X:
                                        print("Yes")
                                        return
                                    elif A[m]*n > X:
                                        break
                                    else:
                                        X = X - A[m]*n
                                        for o in range(N):
                                            for p in range(B[o]+1):
                                                if A[o]*p == X:
                                                    print("Yes")
                                                    return
                                                elif A[o]*p > X:
                                                    break
                                                else:
                                                    X = X - A[o]*p
                                                    for q in range(N):
                                                        for r in range(B[q]+1):
                                                            if A[q]*r == X:
                                                                print("Yes")
                                                                return
                                                            elif A[q]*r > X:
                                                                break
                                                            else:
                                                                X = X - A[q]*r
                                                                for s in range(N):
                                                                    for t in range(B[s]+1):
                                                                        if A[s]*t == X:
                                                                            print("Yes")
                                                                            return
                                                                        elif A[s]*t > X:
                                                                            break
                                                                        else:
                                                                            X = X - A[s]*t
                                                                            for u in range(N):
                                                                                for v in range(B[u]+1):
                                                                                    if A[u]*v == X:
                                                                                        print("Yes")
                                                                                        return
                                                                                    elif A[u]*v > X:
                                                                                        break
                                                                                    else:
                                                                                        X = X - A[u]*v
                                                                                        for w in range(N):
                                                                                            for x in range(B[w]+1):
                                                                                                if A[w]*x == X:
                                                                                                    print("Yes")
                                                                                                    return

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    for i in range(N):
        for j in range(B[i]+1):
            if A[i]*j == X:
                print('Yes')
                return
            X -= A[i]
    print('No')

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #print(A, B)

    for i in range(N):
        for j in range(B[i]+1):
            if A[i]*j == X:
                print("Yes")
                return

    print("No")

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print("N, X", N, X)
    #print("A", A)
    #print("B", B)
    for i in range(N):
        if X >= A[i] * B[i]:
            X -= A[i] * B[i]
        else:
            X -= X // A[i] * A[i]
    if X == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(N):
        for j in range(B[i] + 1):
            if A[i] * j == X:
                print('Yes')
                return
            elif A[i] * j > X:
                break
            else:
                X -= A[i]
    print('No')

=======
Suggestion 6

def main():
    #入力
    N, X = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #最大100枚なので、1~100枚までの全探索
    for i in range(101):
        for j in range(101):
            for k in range(101):
                if i*A[0] + j*A[1] + k*A[2] == X:
                    print("Yes")
                    return
    print("No")

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_, b_ = map(int, input().split())
        a.append(a_)
        b.append(b_)
    for i in range(2**n):
        sum = 0
        for j in range(n):
            if i & (1 << j):
                sum += a[j] * b[j]
        if sum == x:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 8

def main():
    N,X = map(int,input().split())
    A = []
    B = []
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #print(A)
    #print(B)
    for i in range(N):
        for j in range(B[i]+1):
            if A[i]*j == X:
                print("Yes")
                return
    print("No")

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(2 ** n):
        cnt = 0
        for j in range(n):
            if i & (1 << j):
                cnt += a[j][0] * a[j][1]
        if cnt == x:
            print("Yes")
            break
    else:
        print("No")

=======
Suggestion 10

def main():
    #入力
    N,X = map(int,input().split())
    #A_i,B_iを格納するリスト
    A = []
    B = []
    #A_i,B_iを格納
    for i in range(N):
        a,b = map(int,input().split())
        A.append(a)
        B.append(b)
    #合計金額
    sum = 0
    #A_iとB_iを合計
    for i in range(N):
        sum += A[i]*B[i]
    #合計金額がX円以上ならYes
    if sum >= X:
        print("Yes")
    else:
        print("No")
