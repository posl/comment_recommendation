def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B = set(B)
    
    for i in range(N):
        if (N - i) in B:
            continue
        else:
            print(A[N - i - 1])
            break

if __name__ == '__main__':
    main()