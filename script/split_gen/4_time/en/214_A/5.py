def problem214_a():
    n = int(input())
    if n <= 125:
        print(4)
    elif n >= 126 and n <= 211:
        print(6)
    else:
        print(8)
problem214_a()
