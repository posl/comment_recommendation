def main():
    n = int(input())
    a = [input() for _ in range(n)]
    count = {}
    for i in range(n):
        if a[i] not in count:
            count[a[i]] = 0
            print(a[i])
        else:
            count[a[i]] += 1
            print(a[i] + '(' + str(count[a[i]]) + ')')

if __name__ == '__main__':
    main()