def solve():
    N,M,T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = []
    for i in range(M):
        XY.append(list(map(int, input().split())))
    #print(N,M,T,A,XY)
    currentRoom = 1
    currentTime = T
    for i in range(N-1):
        #print("currentRoom: ", currentRoom, "currentTime: ", currentTime)
        if A[i] < currentTime:
            currentTime = currentTime - A[i]
            currentRoom = currentRoom + 1
            #print("currentRoom: ", currentRoom, "currentTime: ", currentTime)
        else:
            break
    #print("currentRoom: ", currentRoom, "currentTime: ", currentTime)
    #print("-----")
    if currentRoom == N:
        print("Yes")
        return
    for i in range(M):
        #print("currentRoom: ", currentRoom, "currentTime: ", currentTime)
        if XY[i][0] < currentRoom:
            continue
        else:
            currentTime = currentTime + XY[i][1]
            currentRoom = XY[i][0]
            #print("currentRoom: ", currentRoom, "currentTime: ", currentTime)
            if currentRoom == N:
                if currentTime > T:
                    print("No")
                    return
                else:
                    print("Yes")
                    return
    print("No")
    return
