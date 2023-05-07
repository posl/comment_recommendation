def main():
    N = int(input())
    ans = 0
    for a in range(1000):
        for b in range(1000):
            if a**3 + a**2*b + a*b**2 + b**3 == N:
                ans = max(ans, a**3 + a**2*b + a*b**2 + b**3)
    print(ans)

if __name__ == '__main__':
    main()