def main():
    A, B = map(int, input().split())
    print(max(A - B * 2, 0))

if __name__ == '__main__':
    main()