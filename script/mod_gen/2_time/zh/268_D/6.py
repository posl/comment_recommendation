def main():
    N = int(input())
    p = list(map(int, input().split()))
    p = [x-1 for x in p]
    ans = 0
    for i in range(N):
        if (p[p[i]] == i):
            ans += 1
    print(ans//2)

if __name__ == '__main__':
    main()