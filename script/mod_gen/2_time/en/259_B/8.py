def main():
    a, b, d = map(int, input().split())
    # a, b, d = map(int, input().split())
    # print(a, b, d)
    d = d * 3.14159265358979323846 / 180
    # print(d)
    # print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))
    print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))

if __name__ == '__main__':
    main()