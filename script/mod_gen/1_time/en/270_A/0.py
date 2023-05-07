def main():
    A, B = map(int, input().split())
    print(A + B - max(A, B) + 1)

if __name__ == '__main__':
    main()