def main():
    x = input()
    m = int(input())
    if len(x) == 1:
        if int(x) <= m:
            print(1)
        else:
            print(0)
        return
    d = int(max(x))
    x = [int(i) for i in x]
    def base_n(x, n):
        x = x[::-1]
        result = 0
        for i in range(len(x)):
            result += x[i] * n**i
        return result
    def check(n):
        return base_n(x, n) <= m
    def binary_search():
        left = d + 1
        right = m + 1
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left - 1
    print(binary_search() - d)

if __name__ == '__main__':
    main()