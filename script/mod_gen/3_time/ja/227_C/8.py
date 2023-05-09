def main():
    N = int(input())
    cnt = 0
    for c in range(1, N+1):
        cnt += (N//c)*(c-1)
        cnt += (N%c)
    print(cnt)

if __name__ == '__main__':
    main()