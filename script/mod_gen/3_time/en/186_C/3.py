def main():
    N = int(input())
    cnt = 0
    for i in range(1, N+1):
        if '7' in str(i) or '7' in oct(i)[2:]:
            continue
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()