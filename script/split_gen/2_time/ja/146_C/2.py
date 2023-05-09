def main():
    A, B, X = map(int, input().split())
    # 二分探索
    left = 0
    right = 10 ** 9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        # midの桁数を求める
        mid_digit = len(str(mid))
        # midの値段を求める
        mid_price = A * mid + B * mid_digit
        # midの値段がX円以下ならrightをmidにする
        if mid_price <= X:
            left = mid
        # midの値段がX円より大きいならleftをmidにする
        else:
            right = mid
    print(left)
