def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    S = sum(A)
    x = T % S
    for i in range(N):
        x -= A[i]
        if x <= 0:
            print(i + 1, A[i] + x)
            break
main()

if __name__ == '__main__':
    main()