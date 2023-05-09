def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = 0
    i = 0
    while i < N and total + A[i] < T:
        total += A[i]
        i += 1
    print(i+1, T-total)

if __name__ == '__main__':
    main()