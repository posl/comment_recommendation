def problem262_a():
    y = int(input())
    while True:
        y += 1
        if y % 4 == 2:
            print(y)
            break
