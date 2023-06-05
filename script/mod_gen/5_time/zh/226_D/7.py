def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    x.sort()
    y.sort()
    if n%2 == 1:
        x_med = x[n//2]
        y_med = y[n//2]
    else:
        x_med = (x[n//2-1]+x[n//2])//2
        y_med = (y[n//2-1]+y[n//2])//2
    ans = 0
    for i in range(n):
        ans += abs(x[i]-x_med) + abs(y[i]-y_med)
    print(ans)

if __name__ == '__main__':
    main()