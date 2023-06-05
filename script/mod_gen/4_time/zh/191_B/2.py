def main():
    n,x = map(int,input().split())
    nums = list(map(int,input().split()))
    for i in range(n):
        if nums[i] != x:
            print(nums[i],end=' ')

if __name__ == '__main__':
    main()