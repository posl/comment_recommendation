def main():
    x = input()
    n = input()
    a = input()
    x = int(x)
    n = int(n)
    a = a.split()
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += int(a[i])
        else:
            sum += int(a[i]) - 1
    if sum <= x:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()