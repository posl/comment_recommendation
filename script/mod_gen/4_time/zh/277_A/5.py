def find_x(p, x):
    for i in range(len(p)):
        if p[i] == x:
            return i + 1

if __name__ == '__main__':
    find_x()