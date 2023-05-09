def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_a = max(A)
    for i in range(N):
        if A[i] == max_a and (i + 1) not in B:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    main()