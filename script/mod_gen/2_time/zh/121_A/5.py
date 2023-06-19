def main():
    h, w = map(int, input().split())
    h1, w1 = map(int, input().split())
    print(h * w - h1 * w - h * w1 + h1 * w1)

if __name__ == '__main__':
    main()