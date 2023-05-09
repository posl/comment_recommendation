def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    if x[i] == x[j] and x[k] == x[l] and y[i] == y[k] and y[j] == y[l]:
                        ans += 1
    print(ans)

if __name__ == '__main__':
    main()