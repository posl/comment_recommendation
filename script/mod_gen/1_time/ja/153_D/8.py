def get_min_attack_count(h):
    if h == 1:
        return 1
    else:
        return get_min_attack_count(h//2) * 2 + 1
h = int(input())
print(get_min_attack_count(h))

if __name__ == '__main__':
    get_min_attack_count()