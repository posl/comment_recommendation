def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    max_num = nums[0]
    sum_num = sum(nums[1:])
    if max_num < sum_num:
        print('Yes')
    else:
        print('No')
