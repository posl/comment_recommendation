def main():
    n = int(input())
    cnt = 0
    for i in range(1, 10**6):
        if i % 2 == 1:
            if n % i == 0:
                cnt += 1
        else:
            if n % i == i // 2:
                cnt += 1
    print(cnt*2)

if __name__ == '__main__':
    main()