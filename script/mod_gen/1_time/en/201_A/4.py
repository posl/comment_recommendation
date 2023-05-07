def is_arithmetic_sequence(a, b, c):
    if a == b and b == c:
        return True
    elif a == b or b == c or c == a:
        return False
    elif a - b == b - c or a - c == c - b or b - a == a - c:
        return True
    else:
        return False
a, b, c = map(int, input().split())
print("Yes" if is_arithmetic_sequence(a, b, c) else "No")

if __name__ == '__main__':
    is_arithmetic_sequence()