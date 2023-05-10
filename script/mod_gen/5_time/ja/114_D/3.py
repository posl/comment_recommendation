def calc_divisor(n):
    # 約数を格納するリスト
    divisors = []
    # 1 から n までの数で n を割った時に余りが 0 になるものを調べる
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            # 見つかった約数をリストに格納
            divisors.append(i)
            # n と割った数が同じでなければ n を割った商も約数になる
            if n // i != i:
                divisors.append(n//i)
    # 約数のリストをソートして出力
    divisors.sort()
    return divisors

if __name__ == '__main__':
    calc_divisor()