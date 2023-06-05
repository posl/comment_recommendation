def main():
    # input
    N = int(input())
    A = list(map(int, input().split()))
    # compute
    max_abs = 0
    for i in range(N):
        for j in range(i+1, N):
            if abs(A[i]-A[j]) > max_abs:
                max_abs = abs(A[i]-A[j])
    # output
    print(max_abs)
    return

if __name__ == '__main__':
    main()