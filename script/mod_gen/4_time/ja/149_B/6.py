def main():
    A, B, K = map(int, input().split())
    if K <= A:
        print(A - K, B)
    else:
        print(0, B - (K - A))

if __name__ == '__main__':
    main()