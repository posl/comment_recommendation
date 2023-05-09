def main():
    N = int(input())
    tlr = [list(map(int, input().split())) for _ in range(N)]
    # 1.各区間の左端と右端をそれぞれリストに格納する
    left = []
    right = []
    for t, l, r in tlr:
        if t == 1:
            left.append(l)
            right.append(r)
        elif t == 2:
            left.append(l)
            right.append(r-1)
        elif t == 3:
            left.append(l+1)
            right.append(r)
        else:
            left.append(l+1)
            right.append(r-1)
    # 2.各区間の左端と右端の組み合わせをカウントする
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if left[i] <= right[j] and left[j] <= right[i]:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()