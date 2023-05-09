def compare(a,b):
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        else:
            return a[i] < b[i]
    return len(a) < len(b)

if __name__ == '__main__':
    compare()