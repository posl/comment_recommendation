def main():
    a, b, x = map(int, input().split())
    if x < a**2*b/2:
        print(math.degrees(math.atan(2*x/(a**2*b))))
    else:
        print(math.degrees(math.atan(a*b**2/(2*(a**2*b-x)))))

if __name__ == '__main__':
    main()