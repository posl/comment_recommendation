def main():
    h, w, c = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(h)]
    ans = 10**18
    for i in range(h):
        for j in range(w):
            for k in range(h):
                for l in range(w):
                    if i == k and j == l:
                        continue
                    ans = min(ans, A[i][j]+A[k][l]+c*(abs(i-k)+abs(j-l)))
    print(ans)

if __name__ == '__main__':
    main()