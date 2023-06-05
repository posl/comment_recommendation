def getup_time():
    A,B,C,D = map(int,input().split())
    if A > C:
        print("高桥")
    elif A < C:
        print("青木")
    elif A == C:
        if B > D:
            print("高桥")
        elif B < D:
            print("青木")
        elif B == D:
            print("高桥")
getup_time()
