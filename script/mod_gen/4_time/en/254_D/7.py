def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i*j <= n and j >= i and i*j % (i+j) == 0:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()