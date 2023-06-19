def sum_of_three_dice():
    a, b, c = map(int, input().split())
    print(21 - a - b - c)

if __name__ == '__main__':
    sum_of_three_dice()