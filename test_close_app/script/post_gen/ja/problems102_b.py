Synthesizing 10/10 solutions (Duplicates hidden)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-1] - A[0])

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-1] - A[0])

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[-1] - a[0])

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(a[n-1] - a[0])

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    diff = [0] * (N - 1)
    for i in range(N-1):
        diff[i] = abs(A[i+1] - A[i])
    print(max(diff))

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    print(A[-1] - A[0])

=======

def main():
    N = int(input())
    A = list(map(int,input().split()))

    A.sort()
    #print(A)

    if N % 2 == 1:
        #奇数
        print(A[N-1] - A[0])
    else:
        #偶数
        print(A[N-1] - A[0])
        print(A[N-2] - A[1])
        print(A[N-1] - A[1])
        print(A[N-2] - A[0])

=======

def main():
    n = int(input())
    a = list(map(int, input().split()))

    # 2つの数値間の絶対値の最大値を求める
    # 1つ目の数値を固定して、残りの数値との差の絶対値の最大値を求める
    # 2つ目の数値を固定して、残りの数値との差の絶対値の最大値を求める
    # 3つ目の数値を固定して、残りの数値との差の絶対値の最大値を求める
    # ...
    # 一番最後の数値を固定して、残りの数値との差の絶対値の最大値を求める
    # という処理を繰り返す
    # これをすべての数値に対して行い、最大値を求める
    max = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if abs(a[i] - a[j]) > max:
                max = abs(a[i] - a[j])

    print(max)
