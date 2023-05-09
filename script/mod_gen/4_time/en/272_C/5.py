def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    even = []
    for i in range(N):
        if A[i]%2 == 0:
            even.append(A[i])
    if len(even) == 0:
        print(-1)
    else:
        print(even[0])

if __name__ == '__main__':
    main()