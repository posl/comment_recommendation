def problems270_b():
    x,y,z = map(int,input().split())
    if (x > 0 and y > 0 and z > 0) or (x < 0 and y < 0 and z < 0) or (x > 0 and y < 0 and z < 0) or (x < 0 and y > 0 and z > 0):
        print(-1)
    else:
        if x > 0:
            print(x + abs(y) + z)
        else:
            print(abs(x) + y + abs(z))
