def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x.append(int(input().split()[0]))
        y.append(int(input().split()[1]))
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] != x[j] and y[i] != y[j]:
                if x[i] in x and y[j] in y:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()