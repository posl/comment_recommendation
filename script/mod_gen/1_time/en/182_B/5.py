def main():
    n = int(input())
    a = list(map(int, input().split()))
    gcdness = [0] * 1001
    for i in a:
        for j in range(2, 1001):
            if i % j == 0:
                gcdness[j] += 1
    print(gcdness.index(max(gcdness)))

if __name__ == '__main__':
    main()