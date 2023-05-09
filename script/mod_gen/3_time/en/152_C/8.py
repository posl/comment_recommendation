def main():
    n = int(input())
    p = list(map(int, input().split()))
    result = 0
    min = n
    for i in range(n):
        if min > p[i]:
            min = p[i]
            result += 1
    print(result)

if __name__ == '__main__':
    main()