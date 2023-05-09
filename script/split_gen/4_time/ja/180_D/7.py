def myCode():
    X,Y,A,B = map(int,input().split())
    cnt = 0
    while X < Y:
        if X * A < X + B:
            X *= A
            cnt += 1
        else:
            cnt += (Y - X - 1) // B
            break
    print(cnt)
