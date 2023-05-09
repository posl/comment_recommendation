def main():
    n, m, x, t, d = map(int, input().split())
    for i in range(x):
        t -= d
    for i in range(m - x):
        t -= 1
    print(t)

if __name__ == '__main__':
    main()