def main():
    N,K = map(int,input().split())
    Sushi = []
    for i in range(N):
        t,d = map(int,input().split())
        Sushi.append((t,d))
    Sushi.sort(key=lambda x:x[1],reverse=True)
    #print(Sushi)
    Left = []
    Right = []
    Left_Topping = {}
    Right_Topping = {}
    Left_Topping[Sushi[0][0]] = 1
    Left.append(Sushi[0])
    Right_Topping[Sushi[-1][0]] = 1
    Right.append(Sushi[-1])
    for i in range(1,N):
        if not Sushi[i][0] in Left_Topping:
            Left_Topping[Sushi[i][0]] = 1
            Left.append(Sushi[i])
        if not Sushi[-i-1][0] in Right_Topping:
            Right_Topping[Sushi[-i-1][0]] = 1
            Right.append(Sushi[-i-1])
    #print(Left)
    #print(Right)
    Left_Total = 0
    Right_Total = 0
    for i in range(len(Left)):
        Left_Total += Left[i][1]
    for i in range(len(Right)):
        Right_Total += Right[i][1]
    #print(Left_Total)
    #print(Right_Total)
    if len(Left) == K:
        print(Left_Total + len(Left)**2)
        return
    if len(Left) == N:
        print(Left_Total + len(Left)**2)
        return
    if len(Right) == K:
        print(Right_Total + len(Right)**2)
        return
    if len(Right) == N:
        print(Right_Total + len(Right)**2)
        return
    Max = 0
    for i in range(len(Left)):
        for j in range(len(Right)):
            if Left[i][0] != Right[j][0]:
                if i+j+1 <= K:
                    if Max < Left_Total + Right_Total + (i+j+1)**2 - Left[i][1] - Right[j][1]:
                        Max = Left_Total + Right_Total + (i+j+1)**2 - Left[i][1] - Right[j][1]
    print(Max)

if __name__ == '__main__':
    main()