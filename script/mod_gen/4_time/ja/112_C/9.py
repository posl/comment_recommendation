def main():
    N = int(input())
    #print(N)
    data = []
    for i in range(N):
        #print(i)
        data.append(input())
        #print(data[i])
    #print(data)
    
    for i in range(N):
        data[i] = data[i].split()
        #print(data[i])
        data[i] = list(map(int, data[i]))
        #print(data[i])
    
    #print(data)
    
    for i in range(N):
        if data[i][2] > 0:
            C_X = data[i][0]
            C_Y = data[i][1]
            H = data[i][2]
            #print(C_X, C_Y, H)
            break
    
    for x in range(101):
        for y in range(101):
            #print(x, y)
            H = H + abs(x - C_X) + abs(y - C_Y)
            #print(H)
            for i in range(N):
                #print(i)
                if data[i][2] != max(H - abs(x - data[i][0]) - abs(y - data[i][1]), 0):
                    #print(data[i][2])
                    #print(max(H - abs(x - data[i][0]) - abs(y - data[i][1]), 0))
                    break
                if i == N - 1:
                    print(x, y, H)
                    exit()

if __name__ == '__main__':
    main()