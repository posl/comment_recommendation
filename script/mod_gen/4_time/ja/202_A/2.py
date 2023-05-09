def reverse_dice(num):
    return 7 - num
a, b, c = map(int, input().split())
print(reverse_dice(a) + reverse_dice(b) + reverse_dice(c))

if __name__ == '__main__':
    reverse_dice()