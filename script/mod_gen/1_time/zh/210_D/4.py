def main():
    h,w,c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(i,h):
                for l in range(j, w):
                    if i == k and j == l:
                        continue
                    ans = min(ans, a[i][j] + a[k][l] + c * (abs(i-k) + abs(j-l)))
    print(ans)

if __name__ == '__main__':
    main()