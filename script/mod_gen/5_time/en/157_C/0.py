def solve():
    n, m = map(int, input().split())
    s = [0] * m
    c = [0] * m
    for i in range(m):
        s[i], c[i] = map(int, input().split())
    if n == 1:
        for i in range(10):
            if i == 0:
                if 1 in s:
                    continue
                else:
                    print(0)
                    return
            if i == c[s.index(1)]:
                print(i)
                return
        print(-1)
        return
    if n == 2:
        for i in range(10):
            for j in range(10):
                if i == 0:
                    if 1 in s:
                        continue
                    else:
                        print(0)
                        return
                if j == 0:
                    if 2 in s:
                        continue
                    else:
                        print(0)
                        return
                if i == c[s.index(1)] and j == c[s.index(2)]:
                    print(i * 10 + j)
                    return
        print(-1)
        return
    if n == 3:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    if i == 0:
                        if 1 in s:
                            continue
                        else:
                            print(0)
                            return
                    if j == 0:
                        if 2 in s:
                            continue
                        else:
                            print(0)
                            return
                    if k == 0:
                        if 3 in s:
                            continue
                        else:
                            print(0)
                            return
                    if i == c[s.index(1)] and j == c[s.index(2)] and k == c[s.index(3)]:
                        print(i * 100 + j * 10 + k)
                        return
        print(-1)
        return

if __name__ == '__main__':
    solve()