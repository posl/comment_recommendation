def main():
    # 读取输入
    nums = input().split(' ')
    # 判断三个数是否相等
    if nums[0] == nums[1] == nums[2]:
        print('否')
    # 判断两个数是否相等
    elif nums[0] == nums[1] or nums[1] == nums[2] or nums[0] == nums[2]:
        print('是')
    else:
        print('否')
