def main():
    x,y,z = map(int, input().split())
    if (x > y and y > z) or (x < y and y < z):
        print(-1)
        return
    if x > y:
        print(x - z)
    else:
        print(z - x)

if __name__ == '__main__':
    main()