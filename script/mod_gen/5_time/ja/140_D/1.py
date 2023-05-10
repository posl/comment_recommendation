def solve(n, k, s):
    # 0回転のときの幸福数を計算
    cnt = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt += 1
    # 1回転のときの幸福数を計算
    cnt2 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt2 += 1
    cnt2 += 2
    # 2回転のときの幸福数を計算
    cnt3 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt3 += 1
    cnt3 += 4
    # 3回転のときの幸福数を計算
    cnt4 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt4 += 1
    cnt4 += 6
    # 4回転のときの幸福数を計算
    cnt5 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt5 += 1
    cnt5 += 8
    # 5回転のときの幸福数を計算
    cnt6 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt6 += 1
    cnt6 += 10
    # 6回転のときの幸福数を計算
    cnt7 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt7 += 1
    cnt7 += 12
    # 7回転のときの幸福数を計算
    cnt8 = 0
    for i in range(1, n):
        if s[i-1] == s[i]:
            cnt8 += 1
    cnt8 +=

if __name__ == '__main__':
    solve()