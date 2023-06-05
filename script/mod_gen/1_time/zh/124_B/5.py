def main():
    n = int(input())
    nums = list(map(int, input().split()))
    cnt = 1
    for i in range(1, n):
        if nums[i-1] <= nums[i]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()