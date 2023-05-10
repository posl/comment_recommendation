def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    count = 0
    for i in range(n):
        count += b[c[i]-1] == a[i]
    print(count)

if __name__ == '__main__':
    main()