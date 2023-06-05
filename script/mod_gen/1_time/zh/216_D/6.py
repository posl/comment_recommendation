def main():
    n, m = map(int, input().split())
    k = [0] * m
    a = [0] * m
    for i in range(m):
        k[i] = int(input())
        a[i] = list(map(int, input().split()))
    print(k)
    print(a)
    # if (n % 2 == 1):
    #     print("No")
    #     exit()
    for i in range(m):
        if (k[i] % 2 == 1):
            print("No")
            exit()
    print("Yes")
    exit()

if __name__ == '__main__':
    main()