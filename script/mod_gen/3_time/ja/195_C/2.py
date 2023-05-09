def main():
    N = int(input())
    cnt = 0
    for i in range(1, len(str(N))+1):
        if N >= 10**(3*i):
            cnt += (N - 10**(3*i) + 1) * i
    print(cnt)

if __name__ == '__main__':
    main()