def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = [0] * (N + 1)
    B[0] = 1
    for i in range(N):
        if B[i] == 0:
            continue
        for a in A:
            if i + a > N:
                break
            B[i + a] = 1
    print(N - B[::-1].index(1))
main()

if __name__ == '__main__':
    main()