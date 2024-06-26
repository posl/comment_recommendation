def main():
    L, R = map(int, input().split())
    ans = 2018
    for i in range(L, min(L+2019, R+1)):
        for j in range(i+1, min(i+2019, R+1)):
            ans = min(ans, (i*j) % 2019)
    print(ans)

if __name__ == '__main__':
    main()