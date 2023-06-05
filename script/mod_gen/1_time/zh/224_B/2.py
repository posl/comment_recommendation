def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    ans = 'Yes'
    for i1 in range(h):
        for i2 in range(i1+1, h):
            for j1 in range(w):
                for j2 in range(j1+1, w):
                    if a[i1][j1]+a[i2][j2] > a[i2][j1]+a[i1][j2]:
                        ans = 'No'
    print(ans)

if __name__ == '__main__':
    main()