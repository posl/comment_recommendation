def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(N):
        if a[i] == count + 1:
            count += 1
    print(count)

if __name__ == '__main__':
    main()