def main():
    n = int(input())
    dice = [list(map(int, input().split())) for i in range(n)]
    cnt = 0
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            cnt += 1
    if cnt > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()