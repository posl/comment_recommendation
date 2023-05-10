def triangle_area(a,b,c):
    #直角三角形の面積を求める関数
    #a,b,cはそれぞれ三角形の辺の長さ
    #三辺の長さを昇順に並び替える
    a,b,c = sorted([a,b,c])
    #直角三角形であるか判定
    if a**2 + b**2 == c**2:
        #面積を求める
        area = a*b/2
    else:
        area = 0
    return int(area)

if __name__ == '__main__':
    triangle_area()