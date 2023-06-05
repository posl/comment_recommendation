def main():
    n = int(input())
    x = []
    y = []
    s = input()
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    flag = False
    for i in range(n):
        if s[i] == 'R':
            for j in range(i+1, n):
                if s[j] == 'L':
                    if x[j] - x[i] == 0:
                        flag = True
                        break
                    elif (y[j] - y[i]) / (x[j] - x[i]) == 1:
                        flag = True
                        break
                else:
                    continue
        else:
            for j in range(i+1, n):
                if s[j] == 'R':
                    if x[i] - x[j] == 0:
                        flag = True
                        break
                    elif (y[i] - y[j]) / (x[i] - x[j]) == 1:
                        flag = True
                        break
                else:
                    continue
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()