def main():
    N = int(input())
    # 七五数の約数の個数
    divisors = 0
    # 約数の個数
    count = 0
    # 七五数の個数
    num = 0
    # 約数の個数が75個になるまでループ
    while count < 75:
        divisors += 1
        # 約数の個数をカウント
        if N % divisors == 0:
            count += 1
    # 七五数の個数をカウント
    while N % divisors == 0:
        num += 1
        N = N // divisors
    print(num)
