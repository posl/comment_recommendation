def main():
    h, w = map(int, input().split())
    h1, w1 = map(int, input().split())
    print((h - h1) * (w - w1))
main()

if __name__ == '__main__':
    main()