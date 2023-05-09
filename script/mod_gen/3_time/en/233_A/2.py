def main():
    x,y = map(int, input().split())
    z = y - x
    if z % 10 == 0:
        print(z // 10)
    else:
        print(z // 10 + 1)

if __name__ == '__main__':
    main()