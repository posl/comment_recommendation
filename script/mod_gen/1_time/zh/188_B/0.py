def main():
    # get input
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # calculate
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    # output
    if sum == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()