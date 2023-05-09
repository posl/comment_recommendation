def main():
    n = int(input())
    s = [input() for _ in range(n)]
    print('
'.join(s[::-1]))

if __name__ == '__main__':
    main()