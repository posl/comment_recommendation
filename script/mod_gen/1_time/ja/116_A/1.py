def main():
    # 入力
    ab, bc, ca = map(int, input().split())
    # 処理
    ans = (ab * bc) // 2
    # 出力
    print(ans)

if __name__ == '__main__':
    main()