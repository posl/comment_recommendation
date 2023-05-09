def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N)]
    ans = 'No'
    cnt = 0
    for i in range(N):
        if D[i][0] == D[i][1]:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            ans = 'Yes'
            break
    print(ans)

if __name__ == '__main__':
    main()