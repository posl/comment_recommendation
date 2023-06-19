def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    ans = 0
    kind = 0
    color = [0]*(10**9+1)
    for i in range(k):
        if color[c[i]] == 0:
            kind += 1
        color[c[i]] += 1
    ans = kind
    for i in range(k,n):
        if color[c[i]] == 0:
            kind += 1
        color[c[i]] += 1
        color[c[i-k]] -= 1
        if color[c[i-k]] == 0:
            kind -= 1
        ans = max(ans,kind)
    print(ans)

if __name__ == '__main__':
    main()