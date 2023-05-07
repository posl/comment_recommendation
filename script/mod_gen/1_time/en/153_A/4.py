def main():
    h, a = map(int, input().split())
    print(h//a + (1 if h%a else 0))
main()

if __name__ == '__main__':
    main()