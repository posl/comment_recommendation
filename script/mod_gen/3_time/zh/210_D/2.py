def main():
    h, w, c = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    ans = float('inf')
    for i in range(h):
        for j in range(w):
            for i2 in range(i,h):
                for j2 in range(j+1,w):
                    ans = min(ans, a[i][j] + a[i2][j2] + c * (abs(i-i2)+abs(j-j2)))
            for i2 in range(i+1,h):
                for j2 in range(j,w):
                    ans = min(ans, a[i][j] + a[i2][j2] + c * (abs(i-i2)+abs(j-j2)))
    print(ans)

if __name__ == '__main__':
    main()