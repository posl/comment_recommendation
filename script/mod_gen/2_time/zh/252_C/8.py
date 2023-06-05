def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    i = 0
    j = 0
    while i < N:
        if j < K and A[i] == B[j]:
            j += 1
        else:
            print("Yes")
            return
        i += 1
    print("No")

if __name__ == '__main__':
    main()