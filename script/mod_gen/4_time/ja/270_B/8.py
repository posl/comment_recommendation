def main():
    x,y,z = map(int, input().split())
    if x > y:
        print(z + abs(x - y) - 1)
    else:
        print(-1)

if __name__ == '__main__':
    main()