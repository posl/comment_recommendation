def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    # 連続部分列の開始位置
    left = 0
    # 連続部分列の終了位置
    right = 0
    # 連続部分列の和
    sum = 0
    while True:
        # 連続部分列の和がK以上になるまで右端を伸ばす
        while right < N and sum < K:
            sum += A[right]
            right += 1
        # 連続部分列の和がK以上になったら、その時点での連続部分列の個数を加算し、左端を右にずらす
        if sum >= K:
            ans += N - right + 1
        # 左端を右にずらす
        sum -= A[left]
        left += 1
        # 左端がNに到達したら終了
        if left == N:
            break
    print(ans)
main()
