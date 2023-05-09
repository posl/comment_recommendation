def main():
    N = int(input())
    X = list(map(int,input().split()))
    ans = 0
    for i in range(1,101):
        ans += sum([(i-j)**2 for j in X])
    print(ans)

if __name__ == '__main__':
    main()