def main():
    N, M = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    L = max(L)
    R = min(R)
    if L <= R:
        print(R - L + 1)
    else:
        print(0)

if __name__ == '__main__':
    main()