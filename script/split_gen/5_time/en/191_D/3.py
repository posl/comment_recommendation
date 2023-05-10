def main():
    X,Y,R = map(float,input().split())
    X = int(X*10000)
    Y = int(Y*10000)
    R = int(R*10000)
    ans = 0
    for i in range(X-R,X+R+1):
        if (R**2-(i-X)**2)**0.5 == int((R**2-(i-X)**2)**0.5):
            ans += int((R**2-(i-X)**2)**0.5)//10000*2+1
        else:
            ans += int((R**2-(i-X)**2)**0.5)//10000*2
    print(ans)
