def median(l):
    l.sort()
    if len(l) % 2 == 0:
        return l[len(l) // 2]
    else:
        return l[len(l) // 2 + 1]

if __name__ == '__main__':
    median()