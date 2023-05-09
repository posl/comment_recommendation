def main():
    N = int(input())
    ans = 0
    for i in range(2, 10**6+1):
        j = 1
        while i**3 + j <= N:
            if i**3 + j == i * j**3:
                ans += 1
            j += 1
    print(ans)

if __name__ == '__main__':
    main()