def main():
    N = int(input())
    dice = []
    for i in range(N):
        dice.append([int(x) for x in input().split()])
    #print(dice)
    for i in range(N-2):
        if dice[i][0] == dice[i][1] and dice[i+1][0] == dice[i+1][1] and dice[i+2][0] == dice[i+2][1]:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()