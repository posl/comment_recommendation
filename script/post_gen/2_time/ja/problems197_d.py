Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 - (y2 - y0) / (2 * N)
    y1 = (y0 + y2) / 2 + (x2 - x0) / (2 * N)
    print(x1, y1)

=======
Suggestion 2

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = (x0 + x2) / 2 + (y2 - y0) * (N / 4) ** 0.5
    y1 = (y0 + y2) / 2 + (x0 - x2) * (N / 4) ** 0.5
    print(x1, y1)

=======
Suggestion 3

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x1 = x2 - x0
    y1 = y2 - y0
    print(x1, y1)

=======
Suggestion 4

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    xN2, yN2 = map(int, input().split())

    dx = xN2 - x0
    dy = yN2 - y0

    x1 = x0 - dx
    y1 = y0 - dy

    print(x1, y1)

=======
Suggestion 5

def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())

    x1 = x0 + (x2 - x0) * (n / 4 - 1) / (n / 2 - 1)
    y1 = y0 + (y2 - y0) * (n / 4 - 1) / (n / 2 - 1)

    print(x1, y1)

=======
Suggestion 6

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = (x0 + x1) / 2 - (y1 - y0) / 2
    y2 = (y0 + y1) / 2 - (x0 - x1) / 2
    print(x2, y2)

=======
Suggestion 7

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    x2 = (x0 + x1) / 2 + (y0 - y1) / (N / 2)
    y2 = (y0 + y1) / 2 + (x1 - x0) / (N / 2)
    print(x2, y2)

=======
Suggestion 8

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x2, y2 = map(int, input().split())
    print((x2 + (x2 - x0)), (y2 + (y2 - y0)))

=======
Suggestion 9

def main():
    N = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    # 三角形の底辺の長さ
    a = ((x1 - x0)**2 + (y1 - y0)**2)**(1/2)
    # 三角形の高さ
    h = a * (3**(1/2)) / 2
    # 三角形の底辺から頂点までの距離
    b = a / 2
    # 三角形の底辺の中点
    x2 = (x0 + x1) / 2
    y2 = (y0 + y1) / 2
    # 三角形の底辺の中点から頂点までの距離
    c = h / 2
    # 三角形の底辺の中点と頂点の角度
    angle = math.atan2(y1 - y0, x1 - x0)
    # 三角形の底辺の中点から頂点までの距離と角度から頂点の座標を求める
    x3 = x2 + b * math.cos(angle + math.pi / 6)
    y3 = y2 + b * math.sin(angle + math.pi / 6)
    print(x3, y3)

=======
Suggestion 10

def main():
    N = int(input())
    x0,y0 = map(int,input().split())
    x1,y1 = map(int,input().split())
    #print(N,x0,y0,x1,y1)
    #print((x1-x0)/(N/2))
    #print((y1-y0)/(N/2))
    X = x0 + (x1-x0)*(N/2-1)/(N/2)
    Y = y0 + (y1-y0)*(N/2-1)/(N/2)
    print(X,Y)
