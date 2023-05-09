def main():
    X, Y, R = map(float, input().split())
    X, Y = int(X*100), int(Y*100)
    R = int(R*100)
    ans = 0
    for x in range(-R, R+1):
        if x*X < 0: continue
        y = int((R**2 - x**2)**0.5)
        if y*Y < 0: continue
        ans += y*2 + 1
    print(ans)

if __name__ == '__main__':
    main()