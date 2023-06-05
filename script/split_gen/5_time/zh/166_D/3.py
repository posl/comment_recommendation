def findAB(x):
    for a in range(1, 1001):
        for b in range(1, 1001):
            if a ** 5 - b ** 5 == x:
                return a, b
            if a ** 5 + b ** 5 == x:
                return a, -b
    return None, None
while True:
    try:
        x = int(input())
        a, b = findAB(x)
        print(a, b)
    except:
        break
