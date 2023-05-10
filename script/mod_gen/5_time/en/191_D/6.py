def main():
    import math
    X, Y, R = map(float, input().split())
    ans = 0
    for i in range(math.ceil(X-R), math.floor(X+R)+1):
        if (R**2 - (X-i)**2)**0.5 % 1 == 0:
            ans += math.floor(Y + (R**2 - (X-i)**2)**0.5) - math.ceil(Y - (R**2 - (X-i)**2)**0.5) + 1
        elif (R**2 - (X-i)**2)**0.5 > 0:
            ans += math.floor(Y + (R**2 - (X-i)**2)**0.5) - math.ceil(Y - (R**2 - (X-i)**2)**0.5)
    print(ans)

if __name__ == '__main__':
    main()