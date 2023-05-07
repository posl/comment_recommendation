def main():
    n,d = map(int, input().split())
    x = []
    for i in range(n):
        x.append(list(map(int, input().split())))
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            tmp = 0
            for k in range(d):
                tmp += (x[i][k]-x[j][k])**2
            if tmp**0.5 == int(tmp**0.5):
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()