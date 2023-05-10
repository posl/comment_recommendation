def main():
    n = int(input())
    dice = [list(map(int,input().split())) for _ in range(n)]
    count = 0
    for i in range(n-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            count += 1
        else:
            pass
    if count >= 1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()