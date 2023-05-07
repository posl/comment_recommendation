def main():
    n = int(input())
    ans = 0
    for a in range(1, int(n**0.5)+1):
        for b in range(1, int(n**0.5)+1):
            c = a*b
            if c > n:
                break
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()