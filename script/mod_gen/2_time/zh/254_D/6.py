def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    # 从左到右，从小到大排序
    left = 0
    while left < N - 1:
        if A[left] > A[left + 1]:
            break
        left += 1
    # 从右到左，从小到大排序
    right = N - 1
    while right > 0:
        if A[right - 1] > A[right]:
            break
        right -= 1
    # 如果整个序列已经排序，我们可以完成
    if left >= right:
        print("Yes")
        exit()
    # 如果K是偶数，我们可以完成
    if K % 2 == 0:
        print("Yes")
        exit()
    # 如果K是奇数，我们不能完成
    print("No")

if __name__ == '__main__':
    main()