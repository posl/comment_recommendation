def count_attack(h):
    if h == 1:
        return 1
    else:
        return 2 * count_attack(h // 2) + 1
h = int(input())
print(count_attack(h))
