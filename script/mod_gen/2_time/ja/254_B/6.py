def main():
    n = int(input())
    for i in range(n):
        for j in range(i+1):
            if j==0 or j==i:
                print(1, end=' ')
            else:
                print(a[i-1][j-1]+a[i-1][j], end=' ')
        print()
        a.append([1]*(i+1))

if __name__ == '__main__':
    main()