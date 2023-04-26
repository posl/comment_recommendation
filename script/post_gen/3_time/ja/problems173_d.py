Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (2 * i - n + 1)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (N - 1 - 2 * i)
    print(ans)

main()

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    ans = 0
    for i in range(N):
        ans += A[i] * (N - i - 1) * (2 * i + 1)

    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i] * (2 ** i)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i] * (i % 2 * 2 - 1)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N):
        ans += A[i] * (2 ** i - 2 ** (N - i - 1))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i + 1)
        ans -= A[i] * (N - i - 1)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    A.sort()
    #print(A)
    ans = 0
    for i in range(N):
        #print(i)
        #print(A[i])
        #print(A[i] * (N - i - 1))
        ans += A[i] * (N - i - 1)
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # 1. 環状に並ぶ人の順番を決める
    # 2. それぞれの人の心地よさを計算する

    # 1. 環状に並ぶ人の順番を決める
    # 降順に並べる
    A = sorted(A, reverse=True)

    # 2. それぞれの人の心地よさを計算する
    # 1番目の人は、2番目の人との距離が最短
    # 2番目の人は、1番目と3番目の人との距離が最短
    # 3番目の人は、2番目と4番目の人との距離が最短
    # 4番目の人は、3番目と5番目の人との距離が最短
    # 5番目の人は、4番目と6番目の人との距離が最短
    # ...
    # 人iは、人i-1と人i+1の距離が最短
    # 人N-1は、人N-2と人Nの距離が最短
    # 人Nは、人N-1と人1の距離が最短
    # 人1は、人Nと人2の距離が最短
    # 人2は、人1と人3の距離が最短
    # 人3は、人2と人4の距離が最短
    # 人4は、人3と人5の距離が最短
    # ...
    # 人iは、人i-2と人i+2の距離が最短
    # 人N-1
