def main():
    n = int(input())
    ans = n
    for i in range(2, int(n**0.5)+1):
        j = 2
        while i**j <= n:
            ans -= 1
            j += 1
    print(ans)

if __name__ == '__main__':
    main()