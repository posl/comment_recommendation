def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_, c_ = map(int, input().split())
        p.append(p_)
        c.append(c_)
    # 最大値
    max = 0
    for i in range(D):
        max += 100 * (i + 1) * p[i] + c[i]
    # 最小値
    min = 0
    for i in range(D):
        min += 100 * (i + 1) * p[i]
    # 最大値を超える
    if G > max:
        print(-1)
        return
    # 最小値を超えない
    if G < min:
        print(0)
        return
    # 最小値を超える
    if G == min:
        print(D)
        return
    # 最大値を超えない
    if G == max:
        print(D)
        return
    # 最小値を超える
    if G > min:
        # 超える問題の番号
        over = 0
        for i in range(D):
            if 100 * (i + 1) * p[i] + c[i] >= G:
                over = i
                break
        # 超える問題の数
        cnt = 0
        for i in range(over):
            cnt += p[i]
        # 超える問題の数
        cnt += (G - 100 * (over + 1) * p[over] - c[over]) // (100 * (over + 1)) + 1
        print(cnt)
        return
main()

if __name__ == '__main__':
    main()