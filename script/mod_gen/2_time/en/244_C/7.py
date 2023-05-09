def main():
    import sys
    n = int(input())
    a = list(range(1, 2 * n + 2))
    for i in range(n + 1):
        print(a[i])
        sys.stdout.flush()
        b = int(input())
        if b == 0:
            break
        a.remove(b)
        a.remove(a[-1])

if __name__ == '__main__':
    main()