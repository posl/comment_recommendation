def attack(num):
    if num == 1:
        return 1
    elif num % 2 == 0:
        return 2 * attack(num / 2) + 1
    else:
        return 2 * attack((num - 1) / 2) + 1
H = int(input())
print(attack(H))
