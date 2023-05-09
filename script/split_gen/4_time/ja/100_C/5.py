def main():
    # 標準入力受付
    n = int(input())
    a = list(map(int, input().split()))
    # 処理
    count = 0
    for i in range(n):
        num = a[i]
        while num % 2 == 0:
            count += 1
            num = num / 2
    # 標準出力
    print(count)
