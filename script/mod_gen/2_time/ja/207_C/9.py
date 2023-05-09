def main():
    N = int(input())
    # 区間の左端と右端をそれぞれリストに格納
    lefts = [0] * N
    rights = [0] * N
    for i in range(N):
        t, l, r = map(int, input().split())
        # 区間の左端と右端をそれぞれリストに格納
        lefts[i] = l
        rights[i] = r
        # 区間の左端と右端をそれぞれリストに格納
        if t == 1:
            lefts[i] = l
            rights[i] = r
        elif t == 2:
            lefts[i] = l
            rights[i] = r - 1
        elif t == 3:
            lefts[i] = l + 1
            rights[i] = r
        elif t == 4:
            lefts[i] = l + 1
            rights[i] = r - 1
    # 区間の左端と右端のリストから、共通部分を持つ区間の組み合わせをカウント
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if lefts[i] <= rights[j] and lefts[j] <= rights[i]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()