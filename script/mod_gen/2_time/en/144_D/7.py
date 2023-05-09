def main():
    a,b,x = map(int,input().split())
    if x <= a**2 * b / 2:
        ans = math.degrees(math.atan(2 * x / (a * b**2)))
    else:
        ans = math.degrees(math.atan(2 * (a**2 * b - x) / (a**3 * b)))
    print(ans)

if __name__ == '__main__':
    main()