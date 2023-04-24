Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    if N == 2:
        if A[0] % 2 == 0 or A[1] % 2 == 0:
            print(max(A))
        else:
            print(-1)
    else:
        A.sort()
        if A[-1] % 2 == 0:
            print(A[-1])
        else:
            print(A[-2])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[0] % 2 == 1:
        print(A[0] + A[1])
    else:
        print(-1)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    if A[0] % 2 == 0:
        print(A[0])
    else:
        for i in range(1, N):
            if A[i] % 2 == 0:
                print(A[i])
                break
        else:
            print(-1)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    for i in range(N-1):
        if A[i] % 2 == 0:
            print(A[i])
            return
    print(-1)

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if a[-1] % 2 == 0:
        print(a[-1])
    elif a[-2] % 2 == 0:
        print(a[-2])
    else:
        print(-1)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    ans = -1
    for i in range(n-1):
        if (a[i] + a[i+1]) % 2 == 0:
            ans = a[i] + a[i+1]
            break
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    A.reverse()
    max = -1
    for i in range(0,N-1):
        for j in range(i+1,N):
            if (A[i] + A[j]) % 2 == 0:
                if max < A[i] + A[j]:
                    max = A[i] + A[j]
    print(max)

=======
Suggestion 8

def main():
    #入力
    N = int(input())
    A = list(map(int,input().split()))
    #初期化
    A.sort(reverse=True)
    #処理
    if A[0]%2 == 0:
        print(A[0])
    else:
        for i in range(1,N):
            if A[i]%2 == 0:
                print(A[i])
                break
        else:
            print(-1)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 最大値を求める
    max_val = max(A)
    # 最大値の桁数を求める
    max_digit = len(str(max_val))
    # 2進数で表した時の桁数を求める
    max_binary_digit = max_digit + 1
    # 2進数で表した時の最大値を求める
    max_binary = pow(2, max_binary_digit)
    # 2進数で表した時の最大値の桁数を求める
    max_binary_digit = len(str(max_binary))

    # 2進数で表した時の各桁の値を求める
    binary = []
    for i in range(max_binary_digit):
        binary.append(pow(2, i))
    binary.reverse()

    # 2進数で表した時の各桁の値を求める
    binary = []
    for i in range(max_binary_digit):
        binary.append(pow(2, i))
    binary.reverse()

    # 2進数で表した時の各桁の値を求める
    binary = []
    for i in range(max_binary_digit):
        binary.append(pow(2, i))
    binary.reverse()

    # 2進数で表した時の各桁の値を求める
    binary = []
    for i in range(max_binary_digit):
        binary.append(pow(2, i))
    binary.reverse()

    # 2進数で表した時の各桁の値を求める
    binary = []
    for i in range(max_binary_digit):
        binary.append(pow(2, i))
    binary.reverse()

    # 2進数で表した時の各桁の値を求める
    binary = []
    for i in range(max_binary_digit):
        binary.append(pow(2, i))
    binary.reverse()

    # 2進数で表した時の各桁の値を求める
    binary = []
    for i in range(max_binary_digit):
        binary.append
