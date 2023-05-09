def solve():
    h,w = map(int,input().split())
    s = [input() for _ in range(h)]
    t = [input() for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                break
        else:
            continue
        break
    else:
        print('No')
        exit()
    for i in range(h):
        for j in range(w):
            if s[i][j] != t[i][j]:
                break
        else:
            continue
        break
    else:
        print('Yes')
        exit()
    print('No')
solve()

if __name__ == '__main__':
    solve()