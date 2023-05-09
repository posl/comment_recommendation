def main():
    N = int(input())
    D = []
    for i in range(N):
        D.append(list(map(int,input().split())))
    cnt = 0
    for i in range(N):
        if D[i][0] == D[i][1]:
            cnt += 1
            if cnt >= 3:
                print('Yes')
                exit()
        else:
            cnt = 0
    print('No')

if __name__ == '__main__':
    main()