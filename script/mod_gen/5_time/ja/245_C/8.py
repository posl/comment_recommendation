def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    if K == 0:
        if A == B:
            print("Yes")
        else:
            print("No")
        return
    if N == 1:
        if abs(A[0] - B[0]) <= K:
            print("Yes")
        else:
            print("No")
        return
    maxA = max(A)
    maxB = max(B)
    minA = min(A)
    minB = min(B)
    if maxA - minB > K or maxB - minA > K:
        print("No")
        return
    print("Yes")

if __name__ == '__main__':
    main()