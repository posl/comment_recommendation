def solution():
    Y = int(input())
    while True:
        Y += 1
        if Y % 4 == 2:
            break
    print(Y)
