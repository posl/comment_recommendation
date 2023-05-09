def main():
    a, b, d = map(int, input().split())
    d = d * 3.141592653589793238462643383279502884197169399375105820974944592307816406286 / 180
    print(a * math.cos(d) - b * math.sin(d), a * math.sin(d) + b * math.cos(d))

if __name__ == '__main__':
    main()