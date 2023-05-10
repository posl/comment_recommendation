def main():
    # input
    X, Y, R = map(float, input().split())
    # compute
    ans = 0
    for i in range(int(X-R), int(X+R+1)):
        for j in range(int(Y-R), int(Y+R+1)):
            if (i-X)**2 + (j-Y)**2 <= R**2:
                ans += 1
    # output
    print(ans)
