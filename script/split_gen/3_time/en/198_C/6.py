def main():
    r, x, y = map(int, input().split())
    dist = (x**2 + y**2)**0.5
    if dist % r == 0:
        print(int(dist/r))
    else:
        print(int(dist/r + 1))
main()
