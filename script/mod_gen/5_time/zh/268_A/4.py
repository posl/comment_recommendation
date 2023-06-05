def main():
    input = raw_input()
    nums = input.split(' ')
    nums = map(int, nums)
    print len(set(nums))

if __name__ == '__main__':
    main()