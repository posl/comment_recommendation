def main():
    import sys
    input = sys.stdin.readline
    from itertools import permutations
    #入力
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    D = list(map(int,input().split()))
    #頂点の座標をリストにまとめる
    P = [A,B,C,D]
    #頂点の座標の組み合わせを全て試す
    for i in permutations(P,4):
        #角度を求める
        #A-B-C
        a = (i[1][0]-i[0][0])*(i[2][0]-i[1][0])+(i[1][1]-i[0][1])*(i[2][1]-i[1][1])
        b = ((i[1][0]-i[0][0])**2+(i[1][1]-i[0][1])**2)**0.5
        c = ((i[2][0]-i[1][0])**2+(i[2][1]-i[1][1])**2)**0.5
        ABC = abs(a)/(b*c)
        #B-C-D
        a = (i[2][0]-i[1][0])*(i[3][0]-i[2][0])+(i[2][1]-i[1][1])*(i[3][1]-i[2][1])
        b = ((i[2][0]-i[1][0])**2+(i[2][1]-i[1][1])**2)**0.5
        c = ((i[3][0]-i[2][0])**2+(i[3][1]-i[2][1])**2)**0.5
        BCD = abs(a)/(b*c)
        #C-D-A
        a = (i[3][0]-i[2][0])*(i[0][0]-i[3][0])+(i[3][1]-i[2][1])*(i[0][1]-i[3][1])
        b = ((i[3][0]-i[2][0])**2+(
