def main():
    h, w = map(int, input().split())
    s = [input() for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            cnt = 0
            for k in range(2):
                for l in range(2):
                    if s[i+k][j+l] == '#':
                        cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()