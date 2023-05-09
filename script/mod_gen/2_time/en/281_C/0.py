def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    total = sum(A)
    t = T % total
    for i in range(N):
        if t < A[i]:
            print(i+1)
            print(t)
            break
        else:
            t -= A[i]

if __name__ == '__main__':
    main()