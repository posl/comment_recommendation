def main():
    N = int(input())
    xy = []
    for i in range(N):
        x,y = map(int, input().split())
        xy.append([x,y])
    xy.sort()
    answer = 0
    for i in range(N):
        for j in range(i+1,N):
            if xy[i][0] == xy[j][0]:
                for k in range(j+1,N):
                    if xy[j][0] == xy[k][0]:
                        for l in range(k+1,N):
                            if xy[k][0] == xy[l][0]:
                                answer += 1
            else:
                break
    print(answer)

if __name__ == '__main__':
    main()