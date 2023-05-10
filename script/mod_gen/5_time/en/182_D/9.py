def robot(a):
    s = 0
    l = [0]
    for i in range(len(a)):
        s += a[i]
        l.append(s)
    return max(l)

if __name__ == '__main__':
    robot()