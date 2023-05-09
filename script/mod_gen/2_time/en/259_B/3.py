def main():
    a, b, d = map(int, input().split())
    rad = math.radians(d)
    a_new = a * math.cos(rad) - b * math.sin(rad)
    b_new = a * math.sin(rad) + b * math.cos(rad)
    print(a_new, b_new)

if __name__ == '__main__':
    main()