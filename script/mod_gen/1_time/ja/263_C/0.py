def main():
    n, m = map(int, input().split())
    for i in range(1, m+1):
        for j in range(i+1, m+1):
            for k in range(j+1, m+1):
                print(i, j, k, sep=' ')

if __name__ == '__main__':
    main()