def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    while True:
        if all([i % 2 == 0 for i in a]):
            a = [i // 2 for i in a]
            cnt += 1
        else:
            break
    print(cnt)

if __name__ == '__main__':
    main()