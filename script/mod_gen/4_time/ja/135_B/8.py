def check(p):
    for i in range(len(p)-1):
        if p[i] > p[i+1]:
            return False
    return True

if __name__ == '__main__':
    check()