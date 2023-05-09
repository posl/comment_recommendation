def solve():
    N = int(input())
    A = list(map(int, input().split()))
    # 各要素の個数をカウント
    cnt = [0] * (10**5+1)
    for a in A:
        cnt[a] += 1
    # 2つの要素の組み合わせの個数をカウント
    cnt2 = [0] * (10**5+1)
    for i in range(10**5+1):
        cnt2[i] = cnt[i] * (cnt[i]-1) // 2
    # 3つの要素の組み合わせの個数をカウント
    cnt3 = [0] * (10**5+1)
    for i in range(10**5+1):
        for j in range(i+1, 10**5+1):
            cnt3[i] += cnt2[i] * cnt[j]
    # 3つの要素の組み合わせの個数を総和
    print(sum(cnt3))
