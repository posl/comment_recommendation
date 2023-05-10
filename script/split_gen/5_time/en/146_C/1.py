def main():
    a, b, x = map(int, input().split())
    #print(a, b, x)
    if a * 10 ** 9 + b * 10 <= x:
        print(10 ** 9)
        return
    if a + b >= x:
        print(0)
        return
    if a * 10 ** 9 + b * 1 >= x:
        print(1)
        return
    if a * 10 ** 9 + b * 2 >= x:
        print(2)
        return
    if a * 10 ** 9 + b * 3 >= x:
        print(3)
        return
    if a * 10 ** 9 + b * 4 >= x:
        print(4)
        return
    if a * 10 ** 9 + b * 5 >= x:
        print(5)
        return
    if a * 10 ** 9 + b * 6 >= x:
        print(6)
        return
    if a * 10 ** 9 + b * 7 >= x:
        print(7)
        return
    if a * 10 ** 9 + b * 8 >= x:
        print(8)
        return
    if a * 10 ** 9 + b * 9 >= x:
        print(9)
        return
    if a * 10 ** 9 + b * 10 >= x:
        print(10)
        return
