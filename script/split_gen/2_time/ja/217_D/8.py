def main():
    L,Q = map(int,input().split())
    #木材の長さ
    length = [L]
    #木材の開始位置
    start = [0]
    #クエリの処理
    for i in range(Q):
        c,x = map(int,input().split())
        if c == 1:
            #木材の長さの更新
            for j in range(len(length)):
                if start[j] <= x < start[j] + length[j]:
                    length[j] = x - start[j]
                    start.insert(j+1,x)
                    length.insert(j+1,start[j+1] + length[j+1] - x)
                    break
        else:
            #木材の長さの出力
            for j in range(len(length)):
                if start[j] <= x < start[j] + length[j]:
                    print(length[j])
                    break
