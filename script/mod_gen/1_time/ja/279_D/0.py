def main():
    A, B = map(int, input().split())
    g = 1
    t = 0
    while A / ((g)**0.5) > t + B:
        g += 1
        t += B
    print(t + A / ((g)**0.5))

if __name__ == '__main__':
    main()