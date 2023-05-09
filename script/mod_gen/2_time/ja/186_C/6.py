def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if "7" in str(i) or "7" in str(oct(i)):
            cnt += 1
    print(N - cnt)

if __name__ == '__main__':
    main()