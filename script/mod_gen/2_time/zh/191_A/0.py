def main():
    n = int(input())
    ans = 0
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            if i%2 != n//i%2:
                ans += 2
    print(ans)

if __name__ == '__main__':
    main()