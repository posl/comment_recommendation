def main():
    H, W = map(int, input().split())
    S = [input() for i in range(H)]
    #print(H, W)
    #print(S)
    # まずは、左上から右下への斜めの線分について、障害物の存在を調べる
    # その後、右上から左下への斜めの線分について、障害物の存在を調べる
    # これらの両方の線分について、障害物の存在を調べることで、
    # 照らされるマスの個数を求めることができる
    # 全てのマスについて、左上から右下への斜めの線分について、障害物の存在を調べる
    # 左上から右下への斜めの線分について、障害物の存在を調べるために、
    # 左上から右下への斜めの線分の個数は、H + W - 1個ある
    # そのため、H + W - 1個の配列を作成し、それぞれの配列について、
    # 左上から右下への斜めの線分について、障害物の存在を調べる
    # 左上から右下への斜めの線分について、障害物の存在を調べるために、
    # 配列の左上から右下への斜めの線分の個数は、H + W - 1個ある
    # そのため、H + W - 1個の配列を作成し、それぞれの配列について、