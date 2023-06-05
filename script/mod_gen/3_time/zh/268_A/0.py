def main():
    a, b, c, d, e = map(int, input().split())
    print(5 - len(set([a, b, c, d, e])))

if __name__ == '__main__':
    main()