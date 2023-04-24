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
        for j in range(B[i] + 1):
            if A[i] * j == X:
                print('Yes')
                exit()

            for k in range(N):
                if i == k:
                    continue
                for l in range(B[k] + 1):
                    if A[i] * j + A[k] * l == X:
                        print('Yes')
                        exit()

    print('No')

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
    print("Yes" if solve(N, X, A, B) else "No")

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        for j in range(B[i]):
            X -= A[i]
            if X == 0:
                print('Yes')
                exit()
    print('No')

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(N):
        if X >= A[i]:
            X -= A[i] * B[i]
    if X == 0:
        print('Yes')
    else:
        print('No')

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
    #print(A)
    #print(B)
    ans = "No"
    for i in range(N):
        for j in range(B[i]+1):
            if A[i]*j==X:
                ans = "Yes"
                break
    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    for i in range(2**N):
        total = 0
        for j in range(N):
            if (i>>j)&1:
                total += A[j]*B[j]
        if total == X:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    for i in range(2 ** n):
        y = 0
        for j in range(n):
            if (i >> j) & 1:
                y += a[j] * b[j]
        if y == x:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    for i in range(N):
        A, B = map(int, input().split())
        X -= A * B
    print("Yes" if X == 0 else "No")

=======
Suggestion 9

def main():
    #入力
    N, X = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    #計算
    for i in range(N):
        X -= A[i] * B[i]
        if X <= 0:
            break

    #出力
    if X == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def solve():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    
    for i in range(N):
        if A[i] <= X:
            X -= A[i] * min(B[i], X // A[i])
    
    if X == 0:
        print("Yes")
    else:
        print("No")
