def func(a, b):
    if a > 0 and b == 0:
        return "Gold"
    elif a == 0 and b > 0:
        return "Silver"
    else:
        return "Alloy"

if __name__ == '__main__':
    func()