def main():
    n, m = map(int, input().split())
    k = [0] * m
    x = [0] * m
    for i in range(m):
        k[i], *x[i] = map(int, input().split())
    for i in range(m):
        for j in range(i+1, m):
            for l in range(k[i]):
                for m in range(k[j]):
                    if x[i][l] == x[j][m]:
                        print("Yes")
                        return
    print("No")

if __name__ == '__main__':
    main()