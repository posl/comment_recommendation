Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    W, H, x, y = map(int, input().split())
    if x == W / 2 and y == H / 2:
        print(W * H / 2, 1)
    else:
        print(W * H / 2, 0)

=======
Suggestion 2

def main():
    W, H, x, y = map(int, input().split())
    if W == x * 2 and H == y * 2:
        print(W * H / 2, 1)
    else:
        print(W * H / 2, 0)

=======
Suggestion 3

def main():
    W, H, x, y = map(int, input().split())
    area = W * H / 2
    if W / 2 == x and H / 2 == y:
        print(area, 1)
    else:
        print(area, 0)

=======
Suggestion 4

def main():
    W,H,x,y = map(int,input().split())
    if W/2 == x and H/2 == y:
        print(W*H/2,1)
    else:
        print(W*H/2,0)
main()

=======
Suggestion 5

def main():
    W,H,x,y = map(int,input().split())
    if W/2 == x and H/2 == y:
        print(W*H/2,1)
    else:
        print(W*H/2,0)

=======
Suggestion 6

def main():
    W, H, x, y = map(int, input().split())
    ans = W * H / 2
    if x * 2 == W and y * 2 == H:
        print(ans, 1)
    else:
        print(ans, 0)

=======
Suggestion 7

def main():
    w, h, x, y = map(int, input().split())
    print(w * h / 2, 1 if w == x * 2 and h == y * 2 else 0)

=======
Suggestion 8

def main():
    W,H,x,y = map(int,input().split())
    area = W*H/2
    if x == W/2 and y == H/2:
        cut = 1
    else:
        cut = 0
    print(area,cut)
