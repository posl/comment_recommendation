def main():
    n = int(input())
    v = list(map(int, input().split()))
    # 1の個数と2の個数を数える
    cnt1 = 0
    cnt2 = 0
    for i in range(n):
        if i % 2 == 0:
            if v[i] == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        else:
            if v[i] == 1:
                cnt2 += 1
            else:
                cnt1 += 1
    # 1の個数と2の個数のうち少ない方の数を書き換える
    if cnt1 < cnt2:
        print(cnt1)
    else:
        print(cnt2)
