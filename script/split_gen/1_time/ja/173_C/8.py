def main():
    # 入力
    h, w, k = map(int, input().split())
    c = [list(input()) for _ in range(h)]
    # 何行選ぶかの組み合わせを全探索
    ans = 0
    for i in range(2**h):
        for j in range(2**w):
            cnt = 0
            for x in range(h):
                for y in range(w):
                    # このマスを選んでいるか
                    is_selected = (i >> x) & 1 == 0 and (j >> y) & 1 == 0
                    if is_selected and c[x][y] == '#':
                        cnt += 1
            if cnt == k:
                ans += 1
    # 出力
    print(ans)
