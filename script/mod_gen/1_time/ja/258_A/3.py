def main():
    # 入力
    K = int(input())
    # 処理
    HH = (21 + K // 60) % 24
    MM = K % 60
    # 出力
    print(f"{HH:02}:{MM:02}")

if __name__ == '__main__':
    main()