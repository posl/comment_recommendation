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
