def main():
    N = int(input())
    x = []
    y = []
    h = []
    for i in range(N):
        x_i, y_i, h_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        h.append(h_i)
    
    #print(x)
    #print(y)
    #print(h)
    
    #print(x[0])
    #print(y[0])
    #print(h[0])
    
    for C_X in range(101):
        for C_Y in range(101):
            for H in range(101):
                #print(C_X, C_Y, H)
                for i in range(N):
                    if h[i] > 0:
                        #print(i)
                        #print(x[i], y[i], h[i])
                        #print(C_X, C_Y, H)
                        #print(abs(x[i]-C_X)+abs(y[i]-C_Y)+H)
                        #print(h[i])
                        if h[i] != max(abs(x[i]-C_X)+abs(y[i]-C_Y)+H, 0):
                            break
                else:
                    print(C_X, C_Y, H)
                    exit()
