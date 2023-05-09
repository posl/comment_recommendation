def main():
    n = int(input())
    p = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n):
        if p[i] > max:
            max = p[i]
            count += 1
    print(count)

if __name__ == '__main__':
    main()