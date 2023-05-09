def main():
    A, B, C = map(int, input().split())
    print(A * B + B * C + C * A + A + B + C)

if __name__ == '__main__':
    main()