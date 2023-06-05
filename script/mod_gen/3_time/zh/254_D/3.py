def solve(n):
    cnt = 0
    # 1の場合は1通り
    if n == 1:
        return 1
    # 2以上の場合
    for i in range(1, n+1):
        # i**2がnを超えるまで繰り返す
        if i**2 > n:
            break
        # i**2がn以下の場合
        for j in range(i, n+1):
            # i*jがnを超えるまで繰り返す
            if i*j > n:
                break
            # i*jがn以下の場合
            cnt += 1
    return cnt

if __name__ == '__main__':
    solve()