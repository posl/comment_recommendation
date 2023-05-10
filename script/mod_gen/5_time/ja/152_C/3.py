def main():
    N = int(input())
    P = list(map(int,input().split()))
    count = 0
    min = N + 1
    for i in P:
        if min > i:
            min = i
            count += 1
    print(count)

if __name__ == '__main__':
    main()