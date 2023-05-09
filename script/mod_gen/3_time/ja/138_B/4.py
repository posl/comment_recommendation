def main():
    n = int(input())
    a = list(map(int, input().split()))
    tmp = 0
    for i in range(n):
        tmp += 1/a[i]
    print(1/tmp)

if __name__ == '__main__':
    main()