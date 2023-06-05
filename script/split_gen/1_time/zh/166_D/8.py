def problem166():
    x = int(input())
    for a in range(1, 1001):
        for b in range(-1000, 0):
            if a**5 - b**5 == x:
                print(a, b)
                return
