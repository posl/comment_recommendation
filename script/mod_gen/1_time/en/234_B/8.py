def main():
    import sys
    import math
    #入力
    readline = sys.stdin.readline
    N = int(readline())
    points = []
    for i in range(N):
        x,y = map(int,readline().split())
        points.append((x,y))
    # 2点間の距離を求める
    def distance(p1,p2):
        return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    # 距離を全探索
    max_distance = 0
    for i in range(N-1):
        for j in range(i+1,N):
            max_distance = max(max_distance,distance(points[i],points[j]))
    # 出力
    print(max_distance)

if __name__ == '__main__':
    main()