def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in d:
        if d[i] % 2 == 1:
            print(i)
            break

if __name__ == '__main__':
    main()