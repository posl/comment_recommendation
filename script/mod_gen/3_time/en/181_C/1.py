def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if x[i] == x[j] == x[k] or y[i] == y[j] == y[k]:
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    main()