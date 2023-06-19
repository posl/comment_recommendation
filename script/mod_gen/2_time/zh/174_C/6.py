def main():
    k = int(input())
    if k%2 == 0:
        print(-1)
    else:
        cnt = 0
        while True:
            cnt += 1
            if int('7'*cnt)%k == 0:
                print(cnt)
                break

if __name__ == '__main__':
    main()