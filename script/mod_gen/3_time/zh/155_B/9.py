def main():
    n = int(input())
    nums = list(map(int,input().split()))
    for num in nums:
        if num % 2 == 0:
            if num % 3 != 0 and num % 5 != 0:
                print("DENIED")
                return
    print("APPROVED")

if __name__ == '__main__':
    main()