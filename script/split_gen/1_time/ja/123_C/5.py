def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min = 0
    for i in range(0, 5):
        if i == 0:
            min = min + 1
        elif i == 1:
            min = min + (n + a - 1) // a
        elif i == 2:
            min = min + (n + b - 1) // b
        elif i == 3:
            min = min + (n + c - 1) // c
        elif i == 4:
            min = min + (n + d - 1) // d
        else:
            min = min + (n + e - 1) // e
    print(min)
