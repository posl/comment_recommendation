def main():
    #n = int(input())
    #a = input().split()
    #a = list(map(int, input().split()))
    n = 4
    a = [1, 1, 3, 2]
    #n = 3
    #a = [1, 1, 1]
    #n = 10
    #a = [2, 2, 4, 1, 1, 1, 4, 2, 2, 1]
    p = 0
    for i in range(n):
        p += a[i]
    print(p - n)

if __name__ == '__main__':
    main()