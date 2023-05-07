def main():
    N = int(input())
    H = list(map(int,input().split()))
    ans = 0
    count = 0
    for i in range(N-1):
        if H[i] >= H[i+1]:
            count += 1
            if count > ans:
                ans = count
        else:
            count = 0
    print(ans)

if __name__ == '__main__':
    main()