def main():
    n = int(input())
    v = list(map(int, input().split()))
    # 1種類の数字があるか
    if len(set(v)) == 1:
        print(n // 2)
        return
    # 2種類の数字がある場合
    # 1種類の数字の数をカウント
    count = 0
    for i in range(n):
        if v[i] == v[0]:
            count += 1
        else:
            break
    # 1種類の数字を前後に並べる
    v1 = v[:count]
    v2 = v[count:]
    v = v1 + v2
    # 1種類の数字の数が偶数か奇数か
    if count % 2 == 0:
        # 偶数の場合
        ans = min(count // 2 + (n - count) // 2, (count + 1) // 2 + (n - count - 1) // 2)
    else:
        # 奇数の場合
        ans = min((count + 1) // 2 + (n - count - 1) // 2, (count - 1) // 2 + (n - count + 1) // 2)
    print(ans)

if __name__ == '__main__':
    main()