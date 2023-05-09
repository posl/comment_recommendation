def main():
    # 入力
    S, T = map(int, input().split())
    # 処理
    ans = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    ans += 1
    # 出力
    print(ans)

if __name__ == '__main__':
    main()