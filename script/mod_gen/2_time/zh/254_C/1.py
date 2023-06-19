def sort_check(a, k):
    for i in range(len(a) - k):
        if a[i] > a[i + k]:
            return False
    return True

if __name__ == '__main__':
    sort_check()