def main():
    n = int(input())
    nums = [int(i) for i in input().split()]
    sum = 0
    for i in range(n-1):
        for j in range(i+1, n):
            sum += nums[i] * nums[j]
    print(sum % (10**9+7))

if __name__ == '__main__':
    main()