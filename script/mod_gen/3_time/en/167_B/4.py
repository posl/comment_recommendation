def main():
    A, B, C, K = map(int, input().split())
    print(min(A, K) - min(B, K - A) if K > A else min(A, K))

if __name__ == '__main__':
    main()