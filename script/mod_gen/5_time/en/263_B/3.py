def main():
    n = int(input())
    p = list(map(int, input().split()))
    max = 0
    for i in range(n):
        count = 0
        j = i
        while True:
            j = p[j] - 1
            count += 1
            if j == -1:
                break
        if max < count:
            max = count
    print(max)
main()

if __name__ == '__main__':
    main()