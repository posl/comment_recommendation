def main():
    h, a = map(int, input().split())
    print(h // a + 1 if h % a else h // a)

if __name__ == '__main__':
    main()