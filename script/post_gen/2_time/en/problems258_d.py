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
    A, B = zip(*sorted(zip(A, B)))
    if X == 1:
        print(A[0])
        return
    if X == 2:
        print(A[0]+B[0])
        return
    if N == 1:
        print(A[0]+B[0]*(X-1))
        return
    if N == 2:
        print(A[0]+min(A[0]+B[0]*(X-2), B[0]*(X-1)))
        return
    if X == N:
        print(sum(B))
        return
    if X == N+1:
        print(sum(B)+A[0])
        return
    if X == N+2:
        print(sum(B)+A[1])
        return
    if X == N+3:
        print(sum(B)+A[1]+B[0])
        return
    if X == N+4:
        print(sum(B)+A[1]+B[0]+B[1])
        return
    if X == N+5:
        print(sum(B)+A[1]+B[0]+B[1]+B[2])
        return
    if X == N+6:
        print(sum(B)+A[1]+B[0]+B[1]+B[2]+B[3])
        return
    if X == N+7:
        print(sum(B)+A[1]+B[0]+B[1]+B[2]+B[3]+B[4])
        return
    if X == N+8:
        print(sum(B)+A[1]+B[0]+B[1]+B[2]+B[3]+B[4]+B[5])
        return
    if X == N+9:
        print(sum(B)+A[1]+B[0]+B[1]+B[2]+B[3]+B[4]+B[5]+B[6])
        return
    if X == N+10:
        print(sum(B)+A[1]+B[0]+B[1]+B[2]+B[3]+

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

    A.sort()
    B.sort()

    ans = 0
    for i in range(N):
        if X == 0:
            break
        if A[i] < B[N-i-1]:
            ans += A[i]
            X -= 1
        else:
            ans += B[N-i-1]
            X -= 1

    if X > 0:
        ans += X * B[0]

    print(ans)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    ans = 0
    for i in range(N):
        if A[i] < B[i]:
            ans += A[i] * X
            X -= 1
        else:
            break
    if X > 0:
        ans += B[i] * X
    print(ans)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    ans = 0
    #Aの最大値がX回未満であれば、AのみのゲームをX回行う
    if X <= N:
        ans = sum(A[0:X])
    else:
        ans = sum(A)
        X -= N
        #Bの最大値がX回未満であれば、BのみのゲームをX回行う
        if X <= N:
            ans += sum(B[0:X])
        else:
            ans += sum(B)
            X -= N
            #Aの最大値とBの最大値の和がX回未満であれば、AとBのゲームをX回行う
            if X <= N:
                ans += (A[-1] + B[-1]) * X
            else:
                ans += (A[-1] + B[-1]) * N
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    #print(A)
    #print(B)
    A.sort()
    B.sort()
    #print(A)
    #print(B)
    ans = 0
    for i in range(N):
        if A[i] < B[N - 1 - i]:
            ans += A[i]
            X -= 1
            if X == 0:
                break
        else:
            ans += B[N - 1 - i]
            X -= 1
            if X == 0:
                break
    if X > 0:
        ans += B[N - 1 - i] * X
    print(ans)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    A.sort()
    B.sort()

    ans = 0
    for i in range(N):
        if A[i] < B[N - 1 - i]:
            ans += A[i]
            X -= 1
        else:
            ans += B[N - 1 - i]
            X -= 1
        if X == 0:
            break

    if X > 0:
        ans += B[N - 1 - i] * X

    print(ans)

main()

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A, B = zip(*sorted(zip(A, B)))
    
    ans = 0
    for i in range(N):
        if X == 1:
            ans += A[i]
            break
        if A[i] < B[i]:
            ans += A[i]
            X -= 1
        else:
            ans += B[i]
            X -= 1
    else:
        ans += B[-1] * X
    print(ans)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    A, B = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A, B = zip(*sorted(zip(A, B)))
    ans = 0
    for i in range(N):
        if X > 1:
            ans += A[i]
            X -= 1
        else:
            break
    ans += B[i] * X
    print(ans)

main()

=======
Suggestion 9

def solve():
    N, X = map(int, input().split())
    A = []
    B = []
    AB = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        AB.append(a + b)
    AB.sort()
    ans = 0
    for i in range(N):
        if i < X:
            ans += AB[i]
        else:
            ans += B[i]
    print(ans)

=======
Suggestion 10

def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(N)]
    AB.sort(key=lambda x: x[0] + x[1])
    ans = 0
    for i in range(N):
        if X > 1:
            ans += AB[i][0]
            X -= 1
        else:
            ans += AB[i][0] + AB[i][1]
            break
    if X > 1:
        ans += (X - 1) * AB[N - 1][1]
    print(ans)
main()
