def main():
    N, M = map(int, input().split())
    x = [list(map(int, input().split())) for _ in range(M)]
    ans = 'Yes'
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            cnt = 0
            for k in range(M):
                if i in x[k] and j in x[k]:
                    cnt += 1
            if cnt == 0:
                ans = 'No'
                break
    print(ans)
main()

if __name__ == '__main__':
    main()