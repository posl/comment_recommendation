def main():
    n,k = map(int,input().split())
    d = [0]*k
    a = [0]*k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int,input().split()))
    snuke = [0]*n
    for i in range(k):
        for j in range(d[i]):
            snuke[a[i][j]-1] += 1
    ans = 0
    for i in range(n):
        if snuke[i] == 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()