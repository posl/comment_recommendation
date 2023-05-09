def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * n
    for i in a:
        cnt[i-1] += 1
    for i in cnt:
        print(i)

if __name__ == '__main__':
    main()