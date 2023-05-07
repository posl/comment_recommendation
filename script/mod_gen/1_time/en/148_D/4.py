def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if A[0] != 1:
        print(-1)
        return
    for i in range(N - 1):
        if A[i] == A[i + 1]:
            continue
        elif A[i] + 1 == A[i + 1]:
            continue
        else:
            print(-1)
            return
    print(N - A[-1])

if __name__ == '__main__':
    main()