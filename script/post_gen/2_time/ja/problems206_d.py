Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N//2):
        if A[i] == A[N-1-i]:
            continue
        elif A[i] == A[i+1] and A[i+1] == A[N-1-i-1]:
            ans += 1
        else:
            ans += 2
    if N % 2 == 1 and A[N//2] != A[N//2+1]:
        ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # N = 8
    # A = [1, 5, 3, 2, 5, 2, 3, 1]
    # N = 7
    # A = [1, 2, 3, 4, 1, 2, 3]
    # N = 1
    # A = [200000]
    # print(A)
    # print(A[::-1])
    # print(N)
    # print(A[:N//2])
    # print(A[N//2+1:])
    # print(A[N//2])
    # print(A[N//2+1])
    # print(A[N//2-1])
    # print(A[N//2-1::-1])
    # print(A[N//2+1:])
    # print(A[N//2+1:][::-1])
    # print(A[N//2-1::-1]==A[N//2+1:])
    # print(A[:N//2]==A[N//2+1:][::-1])
    # print(A[:N//2]==A[N//2+1:])
    # print(A[N//2+1:][::-1]==A[N//2+1:])
    # print(A[:N//2]==A[N//2+1:][::-1])
    # print(A[N//2+1:][::-1]==A[N//2+1:])
    # print(A[:N//2]==A[N//2+1:])
    # print(A[:N//2+1])
    # print(A[N//2:])
    # print(A[:N//2+1]==A[N//2:])
    # print(A[:N//2+1]==A[N//2:][::-1])
    # print(A[:N//2+1][::-1]==A[N//2:])
    # print(A[:N//2+1][::-1]==A[N//2:][::-1])
    # print(A[:N//2+1][::-1]==A[N//2:])
    # print(A[:N//2+1][::-1]==A[N//2:][::-1])
    # print(A[:N//2+1][::-1]==A[N//2:][::-1])
    # print(A

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N//2):
        if A[i] != A[-(i+1)]:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int,input().split()))
    A = [0] + A + [0]
    cnt = 0
    for i in range(1,N+1):
        if A[i] != A[N+1-i]:
            cnt += 1
    print(cnt//2)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(N - max([A.count(i) for i in set(A)]))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    # Aを反転させた配列を作成
    A_rev = A[::-1]
    # AとA_revの各要素を比較し、一致しない要素の数をカウント
    count = 0
    for i in range(N):
        if A[i] != A_rev[i]:
            count += 1
    # countが0の場合は、Aが回文なので0を出力
    if count == 0:
        print(0)
    # countが1の場合は、Aを1回操作するだけで回文にできるので1を出力
    elif count == 1:
        print(1)
    # countが2以上の場合は、Aを2回操作する必要があるので2を出力
    else:
        print(2)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    INF = 10**5+5
    dp = [[INF for _ in range(3)] for _ in range(N+1)]
    dp[0][0] = 0
    dp[0][1] = 1
    dp[0][2] = 2
    for i in range(N):
        dp[i+1][0] = min(dp[i][0], dp[i][1], dp[i][2]) + (A[i] != A[N-i-1])
        dp[i+1][1] = min(dp[i][0]+1, dp[i][1], dp[i][2]) + (A[i] != A[N-i-1])
        dp[i+1][2] = min(dp[i][0]+2, dp[i][1]+1, dp[i][2]) + (A[i] != A[N-i-1])
    print(min(dp[N][0], dp[N][1], dp[N][2]))

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    #print(N)
    #print(A)
    #print("N",N)
    #print("A",A)
    #print("len(A)",len(A))
    #print("len(A)//2",len(A)//2)
    min_count = 0
    for i in range(len(A)//2):
        #print("i",i)
        #print("A[i]",A[i])
        #print("A[-i-1]",A[-i-1])
        if A[i] == A[-i-1]:
            continue
        elif A[i] != A[-i-1]:
            #print("min_count",min_count)
            min_count += 1
    print(min_count)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))

    # Aの中で最も多く出現する数字を求める
    num = [0] * 200001
    for i in range(N):
        num[A[i]] += 1
    max_num = max(num)
    # print(max_num)

    # Aの中で最も多く出現する数字の個数を求める
    max_num_count = 0
    for i in range(200001):
        if num[i] == max_num:
            max_num_count += 1
    # print(max_num_count)

    # Aの中で最も多く出現する数字の個数をNから引いた数が答え
    print(N - max_num_count)
