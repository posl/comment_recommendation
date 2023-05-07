def main():
    #入力
    L1, R1, L2, R2 = map(int, input().split())
    #処理
    if R1 <= L2:
        ans = 0
    elif R2 <= L1:
        ans = 0
    else:
        ans = min(R1, R2) - max(L1, L2)
    #出力
    print(ans)

if __name__ == '__main__':
    main()