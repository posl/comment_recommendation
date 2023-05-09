def exclusive_or(a, b):
    if a == b:
        return a
    if a == 0:
        return exclusive_or(1, b)
    if a % 2 == 0 and b % 2 == 0:
        return exclusive_or(a // 2, b // 2) * 2
    if a % 2 == 0 and b % 2 == 1:
        return exclusive_or(a // 2, b // 2) * 2 + 1
    if a % 2 == 1 and b % 2 == 0:
        return exclusive_or((a - 1) // 2, (b - 1) // 2) * 2 + 1
    if a % 2 == 1 and b % 2 == 1:
        return exclusive_or((a - 1) // 2, (b - 1) // 2) * 2 + 2
a, b = map(int, input().split())
print(exclusive_or(a, b))

if __name__ == '__main__':
    exclusive_or()