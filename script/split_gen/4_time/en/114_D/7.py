def main():
    N = int(input())
    # 約数の数をカウントする
    # 75 = 3^4 * 5^2
    # 75の約数の数は(4+1)*(2+1) = 15個
    # 3^4の約数の数は5個、5^2の約数の数は3個
    # 15 - (5+3) = 7
    # 7個の数字が約数の数になる
    # 75 = 3^4 * 5^2
    # 75の約数の数は(4+1)*(2+1) = 15個
    # 3^4の約数の数は5個、5^2の約数の数は3個
    # 15 - (5+3) = 7
    # 7個の数字が約数の数になる
    ans = 0
    for i in range(1, N+1):
        ans += count_divisors(i)
    print(ans)