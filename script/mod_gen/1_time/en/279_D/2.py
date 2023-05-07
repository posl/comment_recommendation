def main():
    A, B = map(int, input().split())
    g = 1
    t = A
    while t > g * g:
        g += 1
        t = min(t, g * g + B * (g - 1))
    print(t ** 0.5)

if __name__ == '__main__':
    main()