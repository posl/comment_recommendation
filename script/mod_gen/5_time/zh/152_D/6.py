def main():
    n = int(input())
    cnt = 0
    for i in range(n+1):
        if i < 10:
            cnt += 1
        elif i < 100:
            if i % 11 == 0:
                cnt += 1
        else:
            if i % 10 == i // 100:
                cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()