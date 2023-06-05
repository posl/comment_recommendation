def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    # print(x)
    # print(y)
    # print('----------------')
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            x1 = x[i]
            y1 = y[i]
            x2 = x[j]
            y2 = y[j]
            # print(x1,y1,x2,y2)
            a = x1 - x2
            b = y1 - y2
            # print(a,b)
            flag = True
            for k in range(n):
                # print(k)
                x3 = x[k]
                y3 = y[k]
                # print(x3,y3)
                if (x3+a,y3+b) not in zip(x,y):
                    flag = False
                    break
            if flag:
                ans = max(ans, a**2+b**2)
    print(ans)
