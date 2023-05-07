def main():
    n = int(input())
    ans = 0
    for a in range(1,n+1):
        for b in range(a,n//a+1):
            c = n//a//b
            if c < b:
                break
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()