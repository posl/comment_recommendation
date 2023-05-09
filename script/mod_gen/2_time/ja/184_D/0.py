def main():
    A, B, C = map(int, input().split())
    print(A * B / (A + B) + B * C / (B + C) + C * A / (C + A))

if __name__ == '__main__':
    main()