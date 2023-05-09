def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    for i in range(M):
        if B[i] > A[-1]:
            print("No")
            return
        left = 0
        right = N - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == B[i]:
                break
            elif A[mid] < B[i]:
                left = mid + 1
            else:
                right = mid - 1
        if left > right:
            print("No")
            return
        N -= 1
        A.pop(mid)
    print("Yes")

if __name__ == '__main__':
    main()