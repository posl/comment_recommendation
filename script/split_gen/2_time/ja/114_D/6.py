def main():
    N = int(input())
    # 約数の個数を格納するリスト
    divisor = [0] * 1001
    # 約数の個数を数える
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                divisor[j] += 1
    # 七五数の個数を数える
    count = 0
    for i in range(1, 1001):
        if divisor[i] == 75:
            count += 1
    print(count)
