def main():
    w, h, x, y = map(int, input().split())
    print(w*h/2, 1 if w/2 == x and h/2 == y else 0)

if __name__ == '__main__':
    main()