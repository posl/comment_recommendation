def main():
    nums = input().split()
    nums = [int(x) for x in nums]
    print(len(set(nums)))

if __name__ == '__main__':
    main()