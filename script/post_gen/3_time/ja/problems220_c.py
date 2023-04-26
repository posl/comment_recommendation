Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = A * 100
    sum = 0
    for i in range(100 * N):
        sum += B[i]
        if sum > X:
            print(i + 1)
            break

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int,input().split()))
    x = int(input())
    sum = 0
    for i in range(n):
        sum += a[i]
    k = x // sum
    x = x - sum * k
    for i in range(n):
        x = x - a[i]
        if x <= 0:
            print(i+1 + k*n)
            break

=======
Suggestion 3

def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())
    #Aを10**100回連結した数列Bを作成
    B = A * (10**100)
    #Bの項を前から順に足したとき、和が初めてXを超えるのは何項目まで足したとき？を求める
    sum = 0
    for i in range(10**100):
        sum += B[i]
        if sum > X:
            print(i+1)
            break

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int,input().split()))
    x = int(input())
    b = a * 100
    bsum = 0
    for i in range(len(b)):
        bsum += b[i]
        if bsum > x:
            print(i+1)
            break

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    B = []
    for i in range(100):
        B.extend(A)
    print(B)
    sum = 0
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i+1)
            break

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())

    sum_a = sum(a)
    k = 0
    for _ in range(100):
        k += n
        if sum_a * k > x:
            break

    for i in range(n):
        k += 1
        if sum_a * k > x:
            break

    print(k)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())
    B = A * 1000000
    S = 0
    for i in range(1000000*N):
        S += B[i]
        if S > X:
            print(i+1)
            break

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    X = int(input())
    s = sum(A)
    if s <= X:
        print(N*X//s)
    else:
        ans = 0
        for i in range(N):
            ans += 1
            X -= A[i]
            if X <= 0:
                break
        print(ans)

=======
Suggestion 9

def main():
    N=int(input())
    A=list(map(int,input().split()))
    X=int(input())
    B=A
    sumB=sum(A)
    k=0
    while k<X:
        k+=N
        if sumB>0:
            k+=((X-k)//sumB)*N
        for i in range(N):
            k+=1
            if k>X:
                break
            B.append(A[i])
            if k==X:
                break
    print(k)

=======
Suggestion 10

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    X = int(input())
    #初期化
    #B = []
    B = A
    #B = A * 100000
    sum = 0
    #Bを作成
    #for i in range(100000):
    #    B.extend(A)
    #Bを使ってsumを計算
    for i in range(len(B)):
        sum += B[i]
        if sum > X:
            print(i+1)
            break
