def distance(p):
    m = 0
    e = 0
    c = 0
    for i in p:
        m += abs(i)
        e += i**2
        if abs(i) > c:
            c = abs(i)
    e = e**0.5
    print(m)
    print(e)
    print(c)
    return
distance([-3, -1, -4, 1, -5, 9, 2, -6, 5, -3])

if __name__ == '__main__':
    distance()