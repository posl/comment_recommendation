def main():
    n, k = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in range(n)]
    ab.sort()
    for i in range(n):
        if k >= ab[i][0]:
            k += ab[i][1]
        else:
            break
    print(k)

if __name__ == '__main__':
    main()