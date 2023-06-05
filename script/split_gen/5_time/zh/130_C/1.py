def main():
    W,H,x,y = map(int, input().split())
    area = W*H/2
    print(area, end=' ')
    if x*2 == W and y*2 == H:
        print(1)
    else:
        print(0)
