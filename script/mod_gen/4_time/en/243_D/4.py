def main():
    N, X = map(int, input().split())
    S = input()
    ans = X
    for s in S:
        if s == 'L':
            ans = ans*2-1
        elif s == 'R':
            ans = ans*2+1
        else:
            ans = ans//2
    print(ans)

if __name__ == '__main__':
    main()