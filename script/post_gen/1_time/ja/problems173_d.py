Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (2 * i - N + 1)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i - 1) - A[i] * i
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i * 2 - N + 1)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (N - 1 - 2 * i)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (N - 1 - i * 2)
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += A[i] * (i - (N - i))
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[0:N-1]))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A.sort()
    print(sum(A[0::2]))

=======
Suggestion 9

def main():
    #入力
    N = int(input())
    A = list(map(int, input().split()))
    
    #Aを降順にソート
    A.sort(reverse=True)
    
    #Aの降順ソートの最初の要素と最後の要素をそれぞれ最初と最後に配置する
    #その時の心地よさの合計を求める
    ans = A[0] + A[-1]
    
    #Aの降順ソートの2番目からN-1番目の要素をそれぞれ順番に配置する
    #その時の心地よさの合計を求める
    for i in range(1, N-1):
        ans += min(A[i], A[i+1])
    
    #出力
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # A[i] が最大値の人の番号を求める
    max_index = 0
    for i in range(N):
        if A[i] > A[max_index]:
            max_index = i

    # 最大値の人を中心に時計回りに並べる
    B = [0] * N
    for i in range(N):
        B[i] = A[(max_index + i) % N]

    # 時計回りに並べたときの心地よさを求める
    C = [0] * N
    C[0] = 0
    C[1] = B[0]
    for i in range(2, N):
        C[i] = min(C[i-1], B[i-1])

    # 時計回りに並べたときの心地よさの合計を求める
    ans = 0
    for i in range(N):
        ans += C[i]

    print(ans)
