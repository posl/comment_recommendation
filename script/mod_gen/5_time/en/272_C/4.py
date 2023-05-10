def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    even = []
    for i in range(N):
        if A[i] % 2 == 0:
            even.append(A[i])
    if len(even) == 0:
        print(-1)
        exit()
    else:
        for i in range(1, len(even)):
            even[i] += even[i - 1]
    for i in range(N):
        if A[i] % 2 == 1:
            for j in range(len(even)):
                if A[i] + even[j] % 2 == 0:
                    print(A[i] + even[j])
                    exit()
    print(-1)

if __name__ == '__main__':
    main()