def main():
    A, B = map(int, input().split())
    print(A * B - (A + B) + 1)

if __name__ == '__main__':
    main()