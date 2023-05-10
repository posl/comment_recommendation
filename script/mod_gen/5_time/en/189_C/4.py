def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_oranges = 0
    for l in range(n):
        for r in range(l, n):
            for x in range(1, max(a[l:r+1])+1):
                oranges = x * (r - l + 1)
                if oranges > max_oranges:
                    max_oranges = oranges
    print(max_oranges)

if __name__ == '__main__':
    main()