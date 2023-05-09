def main():
    k, x = map(int, input().split())
    print(' '.join(map(str, [x - i for i in range(k - 1, -1, -1)] + [x + i for i in range(1, k)])))

if __name__ == '__main__':
    main()