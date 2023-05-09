def main():
    n = int(input())
    a = list(map(int, input().split()))
    while len(a) > 1:
        a = [min(a), max(a) % min(a)]
        a = [i for i in a if i != 0]
    print(a[0])

if __name__ == '__main__':
    main()