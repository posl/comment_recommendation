def count_attack(h):
    if h == 1:
        return 1
    else:
        return 1 + count_attack(h//2)*2
h = int(input())
print(count_attack(h))

if __name__ == '__main__':
    count_attack()