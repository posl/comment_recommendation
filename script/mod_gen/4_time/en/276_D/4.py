def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if all(i%2 == 0 for i in a):
            a = [i/2 for i in a]
            count += 1
        elif all(i%3 == 0 for i in a):
            a = [i/3 for i in a]
            count += 1
        elif all(i%5 == 0 for i in a):
            a = [i/5 for i in a]
            count += 1
        else:
            break
    if all(i==a[0] for i in a):
        print(count)
    else:
        print(-1)

if __name__ == '__main__':
    main()