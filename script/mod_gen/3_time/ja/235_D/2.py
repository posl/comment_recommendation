def main():
    a, N = map(int, input().split())
    count = 0
    while N > 1:
        if N % a == 0:
            N //= a
        elif N % 10 == 0:
            N //= 10
        else:
            break
        count += 1
    if N == 1:
        print(count)
    else:
        print(-1)

if __name__ == '__main__':
    main()