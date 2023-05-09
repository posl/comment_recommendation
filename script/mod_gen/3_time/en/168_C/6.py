def main():
    a,b,h,m = map(int, input().split())
    theta = 2 * math.pi * ((h + m / 60) / 12 - m / 60)
    print(math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(theta)))

if __name__ == '__main__':
    main()