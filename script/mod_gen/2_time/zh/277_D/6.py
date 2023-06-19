def main():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    b = [0]*m
    for i in range(n):
        b[a[i]%m] += 1
    ans = 0
    for i in range(m):
        if b[i] == 0:
            continue
        ans += i
        b[i] -= 1
        if b[(m-i)%m] != 0:
            b[(m-i)%m] -= 1
        else:
            for j in range(m):
                if b[j] != 0:
                    b[j] -= 1
                    break
    print(ans)

if __name__ == '__main__':
    main()