def check(a, b):
    if a > 0 and b == 0:
        return "Gold"
    elif a == 0 and b > 0:
        return "Silver"
    elif a > 0 and b > 0:
        return "Alloy"

if __name__ == '__main__':
    check()