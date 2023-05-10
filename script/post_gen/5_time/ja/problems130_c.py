Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    w, h, x, y = map(int, input().split())
    s = w * h / 2
    if x == w / 2 and y == h / 2:
        print(s, 1)
    else:
        print(s, 0)

=======
Suggestion 2

def main():
    w,h,x,y = map(int,input().split())
    # 重心を求める
    gx = w/2
    gy = h/2
    # 重心と点(x,y)を結ぶ直線で長方形を二つに分割した時の面積の小さい方を求める
    if gx == x and gy == y:
        print(w*h/2,1)
    else:
        print(w*h/2,0)

=======
Suggestion 3

def main():
    W,H,x,y = map(int,input().split())
    if x == W/2 and y == H/2:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 4

def main():
    w, h, x, y = map(int, input().split())

    # 面積は2つの長方形のうちどちらかが最大になる
    # 2つの長方形のうち大きい方の面積は、長方形の面積の半分になる
    # 2つの長方形のうち小さい方の面積は、長方形の面積の半分になる
    # 2つの長方形のうち小さい方の面積は、長方形の面積の半分になる

    # 最大値は長方形の面積の半分になる
    # 最大値を達成する分割の方法は、長方形の中心を通る直線で分割することになる
    # 長方形の中心は、(w/2, h/2) になる
    # 長方形の中心を通る直線で分割することになる
    # 長方形の中心を通る直線で分割することになる
    # 長方形の中心を通る直線で分割することになる
    # 長方形の中心を通る直線で分割することになる
    # 長方形の中心を通る直線で分割することになる
    # 長方形の中心を通る直線で分割することになる
    # 長方形の中心を通る直線で分割することになる

    # 最大値を達成する分割の方法は、長方形の中心を通る直線で分割することになる
    # 長方形

=======
Suggestion 5

def main():
    W,H,x,y = map(int,input().split())
    print(W*H/2, 1 if W*H/2==x*y else 0)

=======
Suggestion 6

def main():
    W, H, x, y = map(int, input().split())
    print(W * H / 2, end=" ")
    if x * 2 == W and y * 2 == H:
        print(1)
    else:
        print(0)

=======
Suggestion 7

def main():
    W,H,x,y = map(int,input().split())
    if x*2 == W and y*2 == H:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 8

def main():
    w,h,x,y = map(int,input().split())
    print(w*h/2,1 if w/2==x and h/2==y else 0)
