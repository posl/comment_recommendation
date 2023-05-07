def main():
    N = int(input())
    s_x, s_y, t_x, t_y = map(int, input().split())
    x, y, r = [], [], []
    for _ in range(N):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        r.append(c)
    print("Yes" if solve(N, s_x, s_y, t_x, t_y, x, y, r) else "No")

if __name__ == '__main__':
    main()