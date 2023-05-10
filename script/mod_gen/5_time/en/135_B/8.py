def check(p):
    for i in range(1, len(p)):
        if p[i] < p[i-1]:
            return False
    return True

if __name__ == '__main__':
    check()