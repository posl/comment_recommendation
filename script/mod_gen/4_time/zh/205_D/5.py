def main():
    # 读取输入
    input = sys.stdin.readline
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    # 二分法
    def binary_search(a, x):
        left = 0
        right = len(a) - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == x:
                return mid
            elif a[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return left
    # 二分法
    def binary_search2(a, x):
        left = 0
        right = len(a) - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == x:
                return mid
            elif a[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
    # 二分法
    def binary_search3(a, x):
        left = 0
        right = len(a) - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == x:
                return mid
            elif a[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return left
    # 二分法
    def binary_search4(a, x):
        left = 0
        right = len(a) - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == x:
                return mid
            elif a[mid] < x:
                left = mid + 1
            else:
                right = mid - 1
        return right
    # 二分法
    def binary_search5(a, x):
        left = 0
        right = len(a) - 1
        while left <= right:
            mid = (left + right) // 2
            if a[mid] == x:
                return mid
            elif a[mid] < x:
                left = mid + 1

if __name__ == '__main__':
    main()