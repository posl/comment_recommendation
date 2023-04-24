Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t-1])

=======
Suggestion 2

def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t])

=======
Suggestion 3

def main():
    N, Q = map(int, input().split())
    L = []
    for _ in range(N):
        L.append(list(map(int, input().split())))
    for _ in range(Q):
        s, t = map(int, input().split())
        print(L[s-1][t])

=======
Suggestion 4

def main():
    N, Q = map(int, input().split())
    a = []
    for i in range(N):
        a.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = map(int, input().split())
        print(a[s-1][t])

=======
Suggestion 5

def main():
    N, Q = list(map(int, input().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    for i in range(Q):
        s, t = list(map(int, input().split()))
        print(A[s-1][t])

=======
Suggestion 6

def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        L = list(map(int, input().split()))
        A.append(L)
    
    for i in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t])

=======
Suggestion 7

def main():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    S = [0]
    for i in range(N):
        S.append(S[i] + A[i][0])
    for _ in range(Q):
        s, t = map(int, input().split())
        print(A[s-1][t])

=======
Suggestion 8

def main():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    #print(A)
    B = []
    for i in range(N):
        for j in range(1, A[i][0]+1):
            B.append(A[i][j])
    #print(B)
    for _ in range(Q):
        s, t = map(int, input().split())
        print(B[s+t-2])

=======
Suggestion 9

def main():
    N, Q = map(int, input().split())
    # N = 2 * 10 ** 5
    # Q = 2 * 10 ** 5
    # N = 3
    # Q = 4
    # a = []
    # for i in range(N):
    #     a.append(list(map(int, input().split())))
    #     # a[i].append(list(map(int, in

=======
Suggestion 10

def main():
    N, Q = map(int, input().split())
    #各クエリの答えを格納するリスト
    ans = []
    #数列の各項を格納するリスト
    num_list = []
    #各数列の長さを格納するリスト
    num_list_len = []
    #各数列の各項の累積和を格納するリスト
    num_list_sum = []
    #各数列の各項の累積和の累積和を格納するリスト
    num_list_sum_sum = []
    for i in range(N):
        num_list.append(list(map(int, input().split())))
    for i in range(N):
        num_list_len.append(len(num_list[i]))
    for i in range(N):
        num_list_sum.append([0])
        for j in range(num_list_len[i]):
            num_list_sum[i].append(num_list_sum[i][j] + num_list[i][j])
    for i in range(N):
        num_list_sum_sum.append([0])
        for j in range(num_list_len[i] + 1):
            num_list_sum_sum[i].append(num_list_sum_sum[i][j] + num_list_sum[i][j])
    for i in range(Q):
        s, t = map(int, input().split())
        ans.append(num_list_sum_sum[s - 1][t] - num_list_sum_sum[s - 1][0])
    for i in range(Q):
        print(ans[i])
