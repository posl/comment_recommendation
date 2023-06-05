def main():
    n = int(input())
    cnt = 0
    for i in range(1, n+1):
        if '7' in str(i):
            continue
        if '7' in oct(i):
            continue
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()