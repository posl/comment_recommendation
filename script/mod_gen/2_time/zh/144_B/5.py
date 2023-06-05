def main():
    import sys
    a, b = map(int, sys.stdin.readline().split())
    if a >= 1 and a <= 20 and b >= 1 and b <= 20:
        print(a * b)
    else:
        print(-1)

if __name__ == '__main__':
    main()