def main():
    a, b = map(int, input().split())
    print(min(str(a) * b, str(b) * a))

if __name__ == '__main__':
    main()