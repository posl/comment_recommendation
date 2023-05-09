def main():
    # N = int(input())
    # a = list(map(int, input().split()))
    N = 10
    a = [2184, 2126, 1721, 1800, 1024, 2528, 3360, 1945, 1280, 1776]
    cnt = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] = a[i] // 2
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()