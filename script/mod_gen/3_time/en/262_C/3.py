def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] == i + 1:
            count += 1
    print(count // 2)

if __name__ == '__main__':
    main()