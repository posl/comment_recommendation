def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n**0.5)+1):
        for j in range(i, n//i+1):
            if i*j <= n:
                if i == j:
                    ans += 1
                else:
                    ans += 2
    print(ans)

if __name__ == '__main__':
    main()