def main():
    a,N = map(int,input().split())
    count = 0
    while N > 1:
        if N % a == 0:
            N //= a
            count += 1
        elif N % a == 1:
            N -= 1
            count += 1
        else:
            print(-1)
            exit()
    print(count)

if __name__ == '__main__':
    main()