def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    m = 0
    for i in range(N):
        if A[i] > m:
            break
        m += A[i]
    print(m)

if __name__ == '__main__':
    main()