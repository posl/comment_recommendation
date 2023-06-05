def main():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    cnt = 0
    for i in range(n):
        if arr[i] != arr[i-1]:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()