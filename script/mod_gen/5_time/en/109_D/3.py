def main():
    h, w = map(int, input().split())
    a = []
    for i in range(h):
        a.append(list(map(int, input().split())))
    ans = []
    for i in range(h):
        for j in range(w):
            if i == h-1 and j == w-1:
                break
            if a[i][j] % 2 == 1:
                if j == w-1:
                    a[i+1][j] += 1
                    ans.append((i+1, j+1, i+2, j+1))
                else:
                    a[i][j+1] += 1
                    ans.append((i+1, j+1, i+1, j+2))
    print(len(ans))
    for i in ans:
        print(*i)

if __name__ == '__main__':
    main()