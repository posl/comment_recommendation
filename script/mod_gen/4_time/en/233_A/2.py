def main():
    x,y = map(int, input().split())
    if x < y:
        print(y-x)
    else:
        print(0)

if __name__ == '__main__':
    main()