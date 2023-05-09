def main():
    N = int(input())
    ans = 0
    for c in range(1, int(N**(1/3))+1):
        for b in range(1, int(N**(1/2))+1):
            for a in range(1, N+1):
                if a*b*c <= N:
                    ans += 1
                else:
                    break
    print(ans)
    return

if __name__ == '__main__':
    main()