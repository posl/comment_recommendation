def main():
    n = int(input())
    nums = []
    for i in range(n):
        num = input().split()
        if num[0] == '1':
            nums.append(int(num[1]))
        elif num[0] == '2':
            nums = [x+int(num[1]) for x in nums]
        elif num[0] == '3':
            print(min(nums))
            nums.remove(min(nums))

if __name__ == '__main__':
    main()