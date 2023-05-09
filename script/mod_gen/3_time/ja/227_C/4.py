def main():
    N = int(input())
    ans = 0
    for a in range(1, N+1):
        for b in range(a, N+1):
            if a*b > N:
                break
            ans += N//(a*b)
    print(ans)
main()

if __name__ == '__main__':
    main()