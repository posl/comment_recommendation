def main():
    N = int(input())
    ans = 0
    for a in range(1, int(N**0.5)+1):
        for b in range(a, int(N/a**2)+1):
            c = N // (a*b)
            if c >= b:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()