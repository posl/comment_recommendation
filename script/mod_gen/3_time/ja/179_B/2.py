def main():
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N-2):
        if D[i][0] == D[i][1] == D[i+1][0] == D[i+1][1] == D[i+2][0] == D[i+2][1]:
            cnt += 1
    if cnt > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()