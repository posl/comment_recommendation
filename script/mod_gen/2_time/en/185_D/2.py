def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    if M == 0:
        print(1)
        return
    if N == M:
        print(0)
        return
    diff = []
    for i in range(M - 1):
        diff.append(A[i + 1] - A[i] - 1)
    diff.sort(reverse=True)
    if diff[0] == 0:
        print(1)
        return
    print(max(1, (diff[0] - 1) // (M - 1) + 1))

if __name__ == '__main__':
    main()