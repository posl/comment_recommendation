def main():
    n,k = map(int,input().split())
    ab = [list(map(int,input().split())) for _ in range(n)]
    ab.sort(key=lambda x:x[0])
    ans = k
    for a,b in ab:
        if ans < a:
            break
        ans += b
    print(ans)

if __name__ == '__main__':
    main()