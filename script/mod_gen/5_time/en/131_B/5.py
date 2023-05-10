def main():
    n, l = map(int, input().split())
    print(sum(range(l + 1, l + n)) - min(range(l + 1, l + n), key=abs))

if __name__ == '__main__':
    main()