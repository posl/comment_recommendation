def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1,y1 = map(int,input().split())
        x.append(x1)
        y.append(y1)
    x.sort()
    y.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            if x[i] == x[j]:
                continue
            for k in range(j+1,n):
                if y[i] == y[k]:
                    continue
                if x[k] == x[j]:
                    continue
                for l in range(k+1,n):
                    if y[k] == y[l]:
                        continue
                    if x[l] == x[i]:
                        continue
                    if y[i] == y[j]:
                        continue
                    if x[l] == x[k]:
                        continue
                    if y[j] == y[l]:
                        continue
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()