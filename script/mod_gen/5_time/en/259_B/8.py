def main():
    a, b, d = map(int, input().split())
    # d = d % 360
    # print(d)
    # print(a, b, d)
    from math import cos, sin, radians
    # print(cos(radians(d)), sin(radians(d)))
    # print(cos(radians(d)) * a - sin(radians(d)) * b, sin(radians(d)) * a + cos(radians(d)) * b)
    print(cos(radians(d)) * a - sin(radians(d)) * b, sin(radians(d)) * a + cos(radians(d)) * b)

if __name__ == '__main__':
    main()