def main():
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = A[:N//2]
    C = A[N//2:]
    print(sum(B)*L + sum(C)*R)

if __name__ == '__main__':
    main()