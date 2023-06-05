def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # 二分查找
    def binary_search(a, k):
        left = 0
        right = len(a) - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == k:
                return mid
            elif a[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
        return left
    # 二分查找的结果
    result = []
    for i in k:
        index = binary_search(a, i)
        while True:
            if index < len(a) and a[index] == i:
                index += 1
            else:
                result.append(i + index)
                break
    for i in result:
        print(i)

if __name__ == '__main__':
    main()