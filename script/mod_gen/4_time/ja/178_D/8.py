def main():
    n = int(input())
    ans = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if i+j+k == n and i >= 3 and j >= 3 and k >= 3:
                    ans += 1
    print(ans % (10**9+7))

if __name__ == '__main__':
    main()