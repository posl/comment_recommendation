def count_attack(H):
    if H == 1:
        return 1
    else:
        return 2*count_attack(H//2)+1
H = int(input())
print(count_attack(H))

if __name__ == '__main__':
    count_attack()