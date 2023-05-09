def main():
    h, w = map(int, input().split())
    c = [input() for i in range(h)]
    ans = [0]*w
    for i in range(w):
        for j in range(h):
            if c[j][i] == "#":
                ans[i] += 1
    print(*ans)

if __name__ == '__main__':
    main()