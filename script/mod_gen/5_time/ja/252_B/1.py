def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    for i in B:
        A[i-1] = -1
    print("Yes" if max(A) > 0 else "No")

if __name__ == '__main__':
    main()