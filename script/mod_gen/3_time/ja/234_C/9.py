def main():
    K = int(input())
    ans = ""
    while K > 0:
        # 2進数の末尾を取得
        # 0,2のみからなるので、2で割った余りが0,2
        # 余りが0の場合は0を追加
        # 余りが2の場合は2を追加
        ans = str(K % 2) + ans
        # 2進数の末尾を取り除く
        K //= 2
        # 末尾が0の場合は、1を減らす
        if ans[-1] == "0":
            K -= 1
    print(ans)

if __name__ == '__main__':
    main()