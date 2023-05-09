def main():
    N = int(input())
    cnt = 0
    i = 1
    while i < N:
        i += i
        cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()