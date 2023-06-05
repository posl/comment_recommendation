def main():
    n = int(input())
    x = []
    y = []
    h = []
    for i in range(n):
        a,b,c = map(int,input().split())
        x.append(a)
        y.append(b)
        h.append(c)
    
    for C_X in range(0,101):
        for C_Y in range(0,101):
            H = 0
            for i in range(n):
                if h[i] != 0:
                    H = h[i] + abs(x[i]-C_X) + abs(y[i]-C_Y)
                    break
            for i in range(n):
                if h[i] != max(H - abs(x[i]-C_X) - abs(y[i]-C_Y),0):
                    break
            else:
                print(C_X,C_Y,H)
                return
