def main():
    n = int(input())
    # 1桁の数字の個数をカウントする
    # 00, 01, ..., 99
    c1 = [0] * 10
    # 2桁の数字の個数をカウントする
    # 000, 001, ..., 999
    c2 = [0] * 10
    # 3桁の数字の個数をカウントする
    # 0000, 0001, ..., 9999
    c3 = [0] * 10
    for i in range(1, n + 1):
        if i < 10:
            c1[i] += 1
        elif i < 100:
            c2[i // 10] += 1
        else:
            c3[i // 100] += 1
    ans = 0
    for i in range(1, n + 1):
        if i < 10:
            ans += c1[i]
        elif i < 100:
            ans += c2[i % 10]
        else:
            ans += c3[i % 10]
    print(ans)
