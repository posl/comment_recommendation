def main():
    n = int(input())
    dice_list = []
    for i in range(n):
        dice_list.append(list(map(int, input().split())))
    count = 0
    for i in range(n):
        if dice_list[i][0] == dice_list[i][1]:
            count += 1
            if count == 3:
                print('Yes')
                exit()
        else:
            count = 0
    print('No')
