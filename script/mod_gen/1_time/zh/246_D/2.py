def check(x):
    for a in range(100):
        for b in range(100):
            if x == a**3 + a**2*b + a*b**2 + b**3:
                return True
    return False

if __name__ == '__main__':
    check()