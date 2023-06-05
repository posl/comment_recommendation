def getmaxmoney(N,M,X,C,Y):
    maxmoney = 0
    for i in range(N):
        if X[i] == 1:
            money = Y[0]
        else:
            money = 0
        if i == 0:
            maxmoney = money
            continue
        if i == N-1:
            if X[i] == 1:
                if C[i] == 1:
                    money = money + Y[C[i]-1]
                else:
                    money = money + Y[C[i]-1] + Y[C[i]-2]
            else:
                if C[i] == 1:
                    money = 0
                else:
                    money = money + Y[C[i]-2]
            maxmoney = max(maxmoney,money)
            continue
        if X[i] == 1:
            if C[i] == 1:
                money = money + Y[C[i]-1]
            else:
                money = money + Y[C[i]-1] + Y[C[i]-2]
        else:
            if C[i] == 1:
                money = 0
            else:
                money = money + Y[C[i]-2]
        maxmoney = max(maxmoney,money)
    return maxmoney

if __name__ == '__main__':
    getmaxmoney()