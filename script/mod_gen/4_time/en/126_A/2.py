def main():
    n, k = map(int, input().split())
    s = input()
    s = s[:k-1] + s[k-1].lower() + s[k:]
    print(s)
main()

if __name__ == '__main__':
    main()