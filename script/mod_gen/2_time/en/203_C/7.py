def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    i = 0
    while k > 0 and i < n:
        if ab[i][0] - 1 > k:
            break
        else:
            k += ab[i][1] - 1
        i += 1
    print(k + 1)

if __name__ == '__main__':
    main()