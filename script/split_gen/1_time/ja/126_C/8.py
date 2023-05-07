def main():
    N, K = map(int, input().split())
    # 1回目のサイコロ
    ans = 0
    # 2回目以降のサイコロ
    for i in range(1, N+1):
        # 1回目のサイコロでK以上になる確率
        if i >= K:
            ans += 1/N
        # 2回目以降のサイコロでK以上になる確率
        else:
            # 1回目のサイコロの出目
            tmp = i
            # 2回目以降のサイコロの出目
            j = 1
            while tmp < K:
                tmp *= 2
                j += 1
            ans += 1/N * (1/2)**(j-1)
    print(ans)
