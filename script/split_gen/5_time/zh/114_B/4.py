def main():
    s = input()
    nums = []
    for i in range(3, len(s)):
        nums.append(int(s[i-3:i]))
    nums.sort()
    min_diff = 753 - nums[0]
    for i in range(1, len(nums)):
        diff = 753 - nums[i]
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
