def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort()
    for i in range(n):
        if ab[i][0] > k:
            break
        k += ab[i][1]
    print(k)

if __name__ == '__main__':
    main()