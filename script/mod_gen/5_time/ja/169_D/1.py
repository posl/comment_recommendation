def main():
    n = int(input())
    n2 = n
    ans = 0
    for i in range(2, int(n**0.5)+1):
        if n2 % i == 0:
            ans += 1
            n2 //= i
        while n2 % i == 0:
            n2 //= i
    if n2 != 1:
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()