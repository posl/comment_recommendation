def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    sum = 0
    for i in range(n):
        sum += a[i]*b[i]
    if sum == 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()