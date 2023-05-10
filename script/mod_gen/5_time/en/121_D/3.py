def exclusive_or(a, b):
    if a == b:
        return a
    else:
        return 2 * exclusive_or(a // 2, b // 2) + (a % 2 + b % 2) % 2
a, b = map(int, input().split())
print(exclusive_or(a, b))

if __name__ == '__main__':
    exclusive_or()