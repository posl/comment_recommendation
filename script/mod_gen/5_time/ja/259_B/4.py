def main():
    a,b,d = map(int,input().split())
    rad = d * 3.141592653589793238462643383279502884197169399375105820974944592307816406286 / 180
    print(a * math.cos(rad) - b * math.sin(rad), a * math.sin(rad) + b * math.cos(rad))

if __name__ == '__main__':
    main()