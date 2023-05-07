def main():
    A, B = map(int, input().split())
    print(max(A - B - B, 0))

if __name__ == '__main__':
    main()