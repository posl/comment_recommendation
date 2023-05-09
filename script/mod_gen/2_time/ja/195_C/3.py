def main():
    N = int(input())
    cnt = 0
    for i in range(1, len(str(N))+1):
        if i % 3 == 0:
            cnt += (N // (10**i)) * (10**(i-1)) + (N % (10**i) - (10**(i-1) - 1))
        else:
            cnt += (N // (10**i)) * (10**(i-1))
    print(cnt)

if __name__ == '__main__':
    main()