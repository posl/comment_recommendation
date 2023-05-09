def main():
    h, a = map(int, input().split())
    print(h // a + (h % a > 0))

if __name__ == '__main__':
    main()