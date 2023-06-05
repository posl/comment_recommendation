def check_sort(p):
    for i in range(len(p)):
        if p[i] != i + 1:
            return False
    return True

if __name__ == '__main__':
    check_sort()