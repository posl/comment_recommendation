def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = A[K:] + [0] * K
    print(*A)

if __name__ == '__main__':
    main()