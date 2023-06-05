def main():
    n = int(input())
    tlr = []
    for i in range(n):
        tlr.append(list(map(int,input().split())))
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if tlr[i][1] <= tlr[j][2] and tlr[j][1] <= tlr[i][2]:
                count += 1
    print(count)

if __name__ == '__main__':
    main()