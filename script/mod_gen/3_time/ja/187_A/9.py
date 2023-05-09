def main():
    # A, B = map(int, input().split())
    A, B = map(int, '100 999'.split())
    a = A // 100 + (A % 100) // 10 + (A % 100) % 10
    b = B // 100 + (B % 100) // 10 + (B % 100) % 10
    print(max(a, b))

if __name__ == '__main__':
    main()