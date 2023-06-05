def main():
    x,y = map(int,input().split())
    a = y - x
    if a % 10 == 0:
        print(a // 10)
    else:
        print(a // 10 + 1)

if __name__ == '__main__':
    main()