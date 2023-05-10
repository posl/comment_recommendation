def main():
    n = int(input())
    a = input().split()
    count = 0
    for i in range(n):
        if int(a[i]) % 2 != 0:
            count += 1
    print(count)

if __name__ == '__main__':
    main()