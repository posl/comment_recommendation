def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if '7' not in str(i) and '7' not in oct(i)[2:]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()