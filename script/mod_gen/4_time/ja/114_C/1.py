def main():
    n = int(input())
    cnt = 0
    for i in range(3,n+1):
        if '3' in str(i) and '5' in str(i) and '7' in str(i):
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()