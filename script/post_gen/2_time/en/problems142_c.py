Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(*B)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(" ".join(map(str, B)))

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(' '.join(map(str, B)))

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        ans[A[i]-1] = i+1
    print(*ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = [0] * N
    for i in range(N):
        ans[A[i] - 1] = i + 1
    print(*ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    B = [0] * N
    for i in range(N):
        B[A[i] - 1] = i + 1
    print(*B)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # A[i] = j となるようにiを入れる
    # j = 1,2,...,N
    # A[i] = 1 となる i の値を順に出力する
    # その後、A[i] = 2 となる i の値を順に出力する
    # ...
    # A[i] = N となる i の値を順に出力する
    # ということを繰り返す。
    # 1 <= N <= 10^5 なので、O(N) で解ける。
    # A[i] = j となるように i を入れるには、
    # A[i] = j となるような i を順に見ていき、
    # A[i] = j となる i が見つかったら、
    # その i を順に出力していく。
    # その後、A[i] = j+1 となるような i を順に見ていき、
    # A[i] = j+1 となる i が見つかったら、
    # その i を順に出力していく。
    # ...
    # ということを繰り返す。
    # 1 <= N <= 10^5 なので、O(N) で解ける。
    # A[i] = j となるような i を見つけるには、
    # A[i] = j となるような i を順に見ていく。
    # その i を順に出力していく。
    # ということを繰り返す。
    # 1 <= N <= 10^5 なので、O(N) で解ける。
    # A[i] = j となるような i を順に見ていくには、
