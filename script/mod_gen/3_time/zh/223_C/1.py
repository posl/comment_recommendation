def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        temp = input().split()
        a.append(int(temp[0]))
        b.append(int(temp[1]))
    left = 0
    right = 0
    for i in range(n):
        left += a[i] / b[i]
    left /= 2
    for i in range(n):
        if left - a[i] / b[i] > 0:
            left -= a[i] / b[i]
        else:
            right += a[i] / b[i] - left
            left = 0
    print(right)

if __name__ == '__main__':
    main()