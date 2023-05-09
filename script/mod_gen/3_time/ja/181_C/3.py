def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        tmp = input().split()
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if x[i] == x[j] == x[k]:
                    print("Yes")
                    return
                elif x[i] == x[j] or x[i] == x[k] or x[j] == x[k]:
                    continue
                else:
                    if (y[i] - y[j]) / (x[i] - x[j]) == (y[i] - y[k]) / (x[i] - x[k]):
                        print("Yes")
                        return
    print("No")
main()

if __name__ == '__main__':
    main()