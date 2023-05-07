def main():
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    if h == 1 and w == 1:
        print(0)
    elif h == 1 or w == 1:
        print(1)
    else:
        print(4)

if __name__ == '__main__':
    main()