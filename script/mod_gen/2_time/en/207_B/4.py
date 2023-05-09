def main():
    A,B,C,D = map(int,input().split())
    if A <= B*D:
        print(-1)
    else:
        ans = 0
        while A > B*D:
            A += B
            ans += C
        print(ans)

if __name__ == '__main__':
    main()