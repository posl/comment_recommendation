def main():
    n = int(input())
    a = list(map(int, input().split()))
    # 1. 2つの異なる数字があるかどうかを確認する
    # 2. 2つの異なる数字がある場合は、/\/\/\/の条件を満たすために置き換える必要がある
    # 2.1. 置換する場合は、2つの異なる数字のうち、少ない方の出現回数を数える
    # 2.2. 置換しない場合は、2つの異なる数字のうち、多い方の出現回数を数える
    # 3. 2.1と2.2のうち、小さい方が答え
    # 1
    if len(set(a)) == 1:
        print(n // 2)
        return
    # 2
    count = [0] * 100001
    for i in range(n):
        count[a[i]] += 1
    # 2.1
    count1 = 0
    for i in range(100001):
        if count[i] > 0:
            count1 += 1
    # 2.2
    count2 = 0
    for i in range(100001):
        count2 = max(count2, count[i])
    # 3
    print(min(count1, count2))

if __name__ == '__main__':
    main()