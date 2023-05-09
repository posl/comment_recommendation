def main():
    N = int(input())
    q = 2
    cnt = 0
    while q**3 <= N:
        p = 2
        while p < q and p*q**3 <= N:
            cnt += 1
            p += 1
        q += 1
    print(cnt)

if __name__ == '__main__':
    main()