def main():
    num = int(input())
    nums = list(map(int, input().split()))
    max = 0
    sum = 0
    for i in range(num):
        sum += nums[i]
        if sum > max:
            max = sum
    print(max)

if __name__ == '__main__':
    main()