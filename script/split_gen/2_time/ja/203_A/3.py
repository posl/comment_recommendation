def main():
    dice = list(map(int, input().split()))
    dice.sort()
    if dice[0] == dice[1]:
        print(dice[2])
    elif dice[1] == dice[2]:
        print(dice[0])
    else:
        print(0)
