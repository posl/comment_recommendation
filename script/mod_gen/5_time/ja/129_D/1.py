def main():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    # #の数をカウント
    cnt = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                cnt += 1
    # 4方向に照らされるマス数をカウント
    # 4方向に照らされるマス数の最大値を求める
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                continue
            up = 0
            down = 0
            left = 0
            right = 0
            # 上方向
            for k in range(i,-1,-1):
                if s[k][j] == '#':
                    break
                up += 1
            # 下方向
            for k in range(i,h):
                if s[k][j] == '#':
                    break
                down += 1
            # 左方向
            for k in range(j,-1,-1):
                if s[i][k] == '#':
                    break
                left += 1
            # 右方向
            for k in range(j,w):
                if s[i][k] == '#':
                    break
                right += 1
            ans = max(ans,up+down+left+right-3)
    print(ans)

if __name__ == '__main__':
    main()