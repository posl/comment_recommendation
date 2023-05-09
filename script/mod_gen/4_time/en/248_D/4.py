def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    for _ in range(Q):
        L, R, X = map(int, input().split())
        print(sum([1 for a in A[L - 1:R] if a == X]))

if __name__ == '__main__':
    main()