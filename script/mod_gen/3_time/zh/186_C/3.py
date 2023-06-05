def main():
    n = int(input())
    cnt = 0
    for i in range(1, n + 1):
        if '7' in str(i) or '7' in oct(i):
            cnt += 1
    print(n - cnt)
    return 0

if __name__ == '__main__':
    main()