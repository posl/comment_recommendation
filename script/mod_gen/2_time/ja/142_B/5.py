def main():
    n,k = map(int,input().split())
    h = list(map(int,input().split()))
    cnt = 0
    for i in h:
        if i >= k:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()