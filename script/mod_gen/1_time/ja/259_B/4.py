def main():
    a, b, d = map(int,input().split())
    rad = d * math.pi / 180
    print(a * math.cos(rad) - b * math.sin(rad), a * math.sin(rad) + b * math.cos(rad))

if __name__ == '__main__':
    main()