def is_sorted(a):
    for i in range(len(a)-1):
        if a[i+1] < a[i]:
            return False
    return True

if __name__ == '__main__':
    is_sorted()