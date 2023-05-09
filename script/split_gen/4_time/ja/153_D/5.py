def attack(h):
    if h == 1:
        return 1
    else:
        return attack(h//2) * 2 + 1
h = int(input())
print(attack(h))
