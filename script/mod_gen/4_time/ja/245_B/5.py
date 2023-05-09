def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    min_num = 0
    for i in range(n):
        if a[i] == min_num:
            min_num += 1
    print(min_num)

if __name__ == '__main__':
    main()