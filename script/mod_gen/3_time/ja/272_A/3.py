def main():
    # 入力を受け取る
    n = int(input())
    a = list(map(int, input().split()))
    # 答えを出力する
    print(sum(a))

if __name__ == '__main__':
    main()