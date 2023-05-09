def main():
    a, b, d = [int(i) for i in input().split()]
    d = d * math.pi / 180
    a = a * math.cos(d) - b * math.sin(d)
    b = a * math.sin(d) + b * math.cos(d)
    print(a, b)

if __name__ == '__main__':
    main()