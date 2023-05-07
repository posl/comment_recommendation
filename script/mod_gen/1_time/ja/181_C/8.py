def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    #print(p)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if (p[j][0]-p[i][0])*(p[k][1]-p[i][1]) == (p[k][0]-p[i][0])*(p[j][1]-p[i][1]):
                    print('Yes')
                    exit()
    print('No')

if __name__ == '__main__':
    main()