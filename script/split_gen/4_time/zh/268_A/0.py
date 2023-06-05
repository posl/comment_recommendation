def main():
    nums = input().split()
    nums = [int(i) for i in nums]
    print(len(set(nums)))
