def main():
    A, B = map(int, input().split())
    print((B-1)*A/(B*B-1))

if __name__ == '__main__':
    main()