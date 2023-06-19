def problems270_b():
    x,y,z = map(int, input().split())
    if y > 0 or z > 0:
        print(-1)
    else:
        print(x - y - z)
