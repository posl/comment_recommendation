def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(input()))
    for i in range(n):
        for j in range(i+1,n):
            if a[i][j] == 'W' and a[j][i] != 'L':

if __name__ == '__main__':
    main()