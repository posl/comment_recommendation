def main():
    a, b = map(int, input().split())
    print(max(a+b, a+a-1, b+b-1))
main()

if __name__ == '__main__':
    main()