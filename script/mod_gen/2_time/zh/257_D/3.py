def f(x, s, w):
    n = len(s)
    count = 0
    for i in range(n):
        if s[i] == '1':
            if w[i] >= x:
                count += 1
        else:
            if w[i] < x:
                count += 1
    return count

if __name__ == '__main__':
    f()