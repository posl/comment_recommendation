def main():
    L, Q = map(int, input().split())
    mark = [0] * (L + 1)
    mark[0] = 1
    mark[L] = 1
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            mark[x] = 1
        else:
            left = 0
            right = 0
            for i in range(x, L + 1):
                if mark[i] == 1:
                    right = i
                    break
            for i in range(x, -1, -1):
                if mark[i] == 1:
                    left = i
                    break
            print(right - left)

if __name__ == '__main__':
    main()