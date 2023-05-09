def main():
    # get number of test cases
    t = int(input())
    # loop through test cases
    for i in range(t):
        # get number of integers
        n = int(input())
        # split input into list of integers
        a = list(map(int, input().split()))
        # count number of odd integers
        count = 0
        for j in range(n):
            if a[j] % 2 != 0:
                count += 1
        # print number of odd integers
        print(count)

if __name__ == '__main__':
    main()