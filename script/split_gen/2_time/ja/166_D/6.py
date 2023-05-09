def main():
    x = int(input())
    a = 0
    b = 0
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i ** 5 - j ** 5 == x:
                a = i
                b = -j
            elif i ** 5 + j ** 5 == x:
                a = i
                b = j
    print(a, b)
