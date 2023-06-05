def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x.append(int(input().split()[0]))
        y.append(int(input().split()[1]))
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j] or y[i] == y[j]:
                continue
            if x[i] < x[j] and y[i] < y[j]:
                if x[i] in x[j:] and y[i] in y[j:]:
                    ans += 1
            elif x[i] > x[j] and y[i] > y[j]:
                if x[j] in x[i:] and y[j] in y[i:]:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()