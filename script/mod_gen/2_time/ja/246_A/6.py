def main():
    x = []
    y = []
    for i in range(3):
        x.append(int(input().split()[0]))
        y.append(int(input().split()[1]))
    for i in range(3):
        if x.count(x[i]) == 1:
            print(x[i], end=" ")
        if y.count(y[i]) == 1:
            print(y[i])

if __name__ == '__main__':
    main()