def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    s = input()
    flag = False
    for i in range(n):
        if s[i] == 'R':
            for j in range(n):
                if j != i and x[j] > x[i] and y[j] == y[i]:
                    flag = True
                    break
        else:
            for j in range(n):
                if j != i and x[j] < x[i] and y[j] == y[i]:
                    flag = True
                    break
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()