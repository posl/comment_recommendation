def main():
    N = int(input())
    XY = [list(map(int,input().split())) for _ in range(N)]
    S = input()
    for i in range(N):
        if S[i] == 'R':
            XY[i][1] += 1
        else:
            XY[i][1] -= 1
    XY.sort()
    #print(XY)
    for i in range(N-1):
        if XY[i][1] == XY[i+1][1]:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()