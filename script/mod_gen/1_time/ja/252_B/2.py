def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxA = max(A)
    for i in range(K):
        if B[i] == A.index(maxA) + 1:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()