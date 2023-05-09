def main():
    n, m, x, t, d = map(int, input().split())
    if m < x:
        print(t + (n - x) * d)
    else:
        print(t - (x - m) * d)

if __name__ == '__main__':
    main()