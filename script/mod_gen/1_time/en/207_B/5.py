def main():
    A,B,C,D = map(int,input().split())
    if A > D*C:
        print(-1)
        return
    ans = 0
    while A > B*D:
        ans += 1
        A += (B-C)
    print(ans)

if __name__ == '__main__':
    main()