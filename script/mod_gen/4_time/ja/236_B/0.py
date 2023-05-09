def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = {}
    for i in range(4*N-1):
        if A[i] in B:
            B[A[i]] += 1
        else:
            B[A[i]] = 1
    for i in B:
        if B[i] % 2 == 1:
            print(i)
            break

if __name__ == '__main__':
    main()