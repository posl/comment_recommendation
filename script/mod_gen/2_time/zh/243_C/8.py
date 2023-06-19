def main():
    N = int(input())
    XY = []
    for i in range(N):
        XY.append(list(map(int, input().split())))
    S = input()
    #print(N, XY, S)
    #print(XY[0][0])
    for i in range(N):
        if S[i] == 'R':
            XY[i][0] += 1
        else:
            XY[i][0] -= 1
    #print(XY)
    for i in range(N):
        for j in range(i+1, N):
            if XY[i] == XY[j]:
                print('Yes')
                return
    print('No')
    return

if __name__ == '__main__':
    main()