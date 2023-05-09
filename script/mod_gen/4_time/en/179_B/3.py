def main():
    N = int(input())
    dice = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        if dice[i][0] == dice[i][1]:
            cnt += 1
        else:
            cnt = 0
        if cnt == 3:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()