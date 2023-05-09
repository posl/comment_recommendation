def main():
    n, m, x, t, d = map(int, input().split())
    for i in range(m, n):
        if i < x:
            t += d
        else:
            break
    print(t)

if __name__ == '__main__':
    main()