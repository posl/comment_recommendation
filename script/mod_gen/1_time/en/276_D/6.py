def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    while True:
        if len(set(a)) == 1:
            print(count)
            break
        if all([i % 2 == 0 for i in a]):
            a = [i / 2 for i in a]
            count += 1
        elif all([i % 3 == 0 for i in a]):
            a = [i / 3 for i in a]
            count += 1
        else:
            print(-1)
            break

if __name__ == '__main__':
    main()