def main():
    A, B, K = map(int, input().split())
    print(max(0, A-K), max(0, B-max(0, K-A)))

if __name__ == '__main__':
    main()