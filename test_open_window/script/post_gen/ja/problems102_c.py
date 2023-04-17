Synthesizing 8/10 solutions

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - i - 1 for i in range(N)]
    A.sort()
    b = A[N//2]
    ans = 0
    for i in range(N):
        ans += abs(A[i] - b)
    print(ans)

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [A[i] - i for i in range(N)]
    A.sort()
    b = A[N // 2]
    print(sum([abs(A[i] - b) for i in range(N)]))

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    b = N // 2
    print(sum([abs(A[i] - (b + i + 1)) for i in range(N)]))

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # A_i - (b + i) の絶対値の総和の最小値を求める
    # A_i - (b + i) の絶対値の最小値は、A_i - (b + i) の符号が一致している場合に
    # その値になるので、A_i - (b + i) の符号が一致している場合には、そのままの値を
    # 一致していない場合には、その値の絶対値を加算する
    # ここで、A_i - (b + i) の符号が一致している場合には、そのままの値を
    # 一致していない場合には、その値の絶対値を加算する
    # ここで、A_i - (b + i) の符号が一致している場合には、そのままの値を
    # 一致していない場合には、その値の絶対値を加算する
    # ここで、A_i - (b + i) の符号が一致している場合には、そのままの値を
    # 一致していない場合には、その値の絶対値を加算する
    # ここで、A_i - (b + i) の符号が一致している場合には、そのままの値を
    # 一致していない場合には、その値の絶対値を加算する
    # ここで、A_i - (b + i) の符号が一致している場合には、そのままの値を
    # 一致していない場合には、その値の

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    #print(A)
    B = [0] * N
    for i in range(N):
        B[i] = A[i] - i - 1
    #print(B)
    B.sort()
    #print(B)
    if N % 2 == 0:
        ans = 0
        for i in range(N):
            ans += abs(B[i] - B[N//2 - 1])
        print(ans)
    else:
        ans1 = 0
        ans2 = 0
        for i in range(N):
            ans1 += abs(B[i] - B[N//2])
            ans2 += abs(B[i] - B[N//2 - 1])
        print(min(ans1, ans2))

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # A.sort()
    # print(A)
    # print(A[N//2])
    # print(A[N//2-1])
    # print(A[N//2] - A[N//2-1])
    # print(A[N//2-1] - A[N//2])
    # print(A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2])
    # print(A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2] + A[N//2] - A[N//2-1])
    # print(A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2] + A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2])
    # print(A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2] + A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2] + A[N//2] - A[N//2-1])
    # print(A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2] + A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2] + A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2])
    # print(A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2] + A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2] + A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2] + A[N//2] - A[N//2-1])
    # print(A[N//2] - A[N//2-1] + A[N//2-1] - A[N//2] +

=======

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #Aの中央値のindexを求める
    A.sort()
    #print(A)
    b = A[(N-1)//2]
    #print(b)
    ans = 0
    for i in range(N):
        ans += abs(A[i]-(b+i))
    print(ans)

=======

def read_int():
    return int(input())
