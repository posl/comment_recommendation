def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        tmp = input().split()
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            ans = max(ans, (x[i]-x[j])**2 + (y[i]-y[j])**2)
    print(ans**0.5)

if __name__ == '__main__':
    main()