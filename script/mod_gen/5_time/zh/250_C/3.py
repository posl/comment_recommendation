def swap(x, i):
    if x[i] == i + 1:
        return x
    else:
        tmp = x[i]
        x[i] = x[i + 1]
        x[i + 1] = tmp
        return x

if __name__ == '__main__':
    swap()