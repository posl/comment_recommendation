def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if x[i] == x[j] and x[j] == x[k]:
                    print("Yes")
                    return
                elif y[i] == y[j] and y[j] == y[k]:
                    print("Yes")
                    return
                elif (y[i]-y[j])*(x[i]-x[k]) == (y[i]-y[k])*(x[i]-x[j]):
                    print("Yes")
                    return
    print("No")

if __name__ == '__main__':
    main()