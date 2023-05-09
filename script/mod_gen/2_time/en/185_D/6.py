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
    if M == 1:
        print(1)
        return
    if M == 2:
        print(2)
        return
    d = []
    for i in range(M-1):
        d.append(A[i+1] - A[i] - 1)
    d.sort(reverse=True)
    k = 1
    for i in range(M-2):
        k = max(k, d[i] + 1)
    print((k + 1) // 2)
main()

if __name__ == '__main__':
    main()