def main():
    nums = list(map(int, input().split()))
    for i in range(1, 6):
        if nums[i - 1] == 0:
            print(i)

if __name__ == '__main__':
    main()