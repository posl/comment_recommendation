def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    sum = 0
    for i in range(k):
        sum += p[i]
    print(sum)

if __name__ == '__main__':
    main()