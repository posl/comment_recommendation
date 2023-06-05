def main():
    N = int(input())
    ans = 0
    for i in range(1, 10**6):
        if i % 2 == 1:
            if N % i == 0:
                ans += 1
        else:
            if N % i == i // 2:
                ans += 1
    print(ans * 2)

if __name__ == '__main__':
    main()