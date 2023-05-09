def main():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    x.sort()
    y.sort()
    x_diff = []
    y_diff = []
    for i in range(N-1):
        x_diff.append(x[i+1]-x[i])
        y_diff.append(y[i+1]-y[i])
    x_diff.sort(reverse=True)
    y_diff.sort(reverse=True)
    x_ans = 0
    y_ans = 0
    for i in range(N-1):
        x_ans += x_diff[i]*(i+1)
        y_ans += y_diff[i]*(i+1)
    print(x_ans*y_ans)

if __name__ == '__main__':
    main()