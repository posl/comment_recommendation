def main():
    n, m = map(int, input().split())
    a = [input() for _ in range(2*n)]
    win = [[0]*m for _ in range(2*n)]
    for i in range(m):
        for j in range(n):
            a1 = a[2*j]
            a2 = a[2*j+1]
            if a1[i] == a2[i]:
                continue
            if a1[i] == 'G' and a2[i] == 'C':
                win[2*j][i] = 1
            elif a1[i] == 'C' and a2[i] == 'P':
                win[2*j][i] = 1
            elif a1[i] == 'P' and a2[i] == 'G':
                win[2*j][i] = 1
            else:
                win[2*j+1][i] = 1
    for i in range(2*n):
        print(i+1, sum(win[i]))

if __name__ == '__main__':
    main()