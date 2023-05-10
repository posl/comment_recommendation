def main():
    n = int(input())
    dice = []
    for i in range(n):
        a,b = input().split()
        dice.append([int(a),int(b)])
    count = 0
    for j in range(n-2):
        if dice[j][0] == dice[j][1] and dice[j+1][0] == dice[j+1][1] and dice[j+2][0] == dice[j+2][1]:
            count += 1
    if count > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()