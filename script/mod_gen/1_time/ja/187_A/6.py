def main():
    a, b = map(int, input().split())
    a = sum(map(int, str(a)))
    b = sum(map(int, str(b)))
    print(max(a, b))

if __name__ == '__main__':
    main()