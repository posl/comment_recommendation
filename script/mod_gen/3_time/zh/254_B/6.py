def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append([1]*(i+1))
        for j in range(1,i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]
    for i in range(n):
        for j in range(i+1):
            if j == i:
                print(a[i][j])
            else:
                print(a[i][j],end=" ")

if __name__ == '__main__':
    main()