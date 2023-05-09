def main():
    #入力
    N, T = map(int, input().split())
    c_t_list = [list(map(int, input().split())) for _ in range(N)]
    #処理
    c_t_list.sort(key=lambda x: x[1])
    ans = 1001
    for c_t in c_t_list:
        if c_t[1] <= T:
            ans = min(ans, c_t[0])
    #出力
    if ans == 1001:
        print("TLE")
    else:
        print(ans)
