def main():
    X, Y, R = map(float, input().split())
    X = int(X*10)
    Y = int(Y*10)
    R = int(R*10)
    ans = 0
    for x in range(int(X-R), int(X+R)+1):
        for y in range(int(Y-R), int(Y+R)+1):
            if (x-X)**2 + (y-Y)**2 <= R**2:
                ans += 1
    print(ans)
