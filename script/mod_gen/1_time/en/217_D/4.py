def main():
    L, Q = map(int, input().split())
    cut = [0] * (L + 1)
    cut[0] = 1
    cut[L] = 1
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            cut[x] = 1
        else:
            ans = 0
            for i in range(x, L + 1):
                if cut[i] == 1:
                    ans = i - x
                    break
            print(ans)

if __name__ == '__main__':
    main()