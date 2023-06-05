def main():
    k = int(input())
    cnt = 0
    for i in range(1, k + 1):
        cnt = cnt * 10 + 7
        cnt %= k
        if cnt == 0:
            print(i)
            return
    print(-1)

if __name__ == '__main__':
    main()