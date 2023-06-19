def problem270_b():
    x,y,z = map(int,input().split())
    if x > y > z or x > z > y:
        print(-1)
    else:
        print(x + z)
