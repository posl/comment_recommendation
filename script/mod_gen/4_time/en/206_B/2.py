def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        cnt += i
        if cnt >= N:
            print(i)
            break

if __name__ == '__main__':
    main()