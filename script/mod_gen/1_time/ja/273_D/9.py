def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    block = [[0, 0, 0, 0] for _ in range(N)]
    for i in range(N):
        r_i, c_i = map(int, input().split())
        block[i] = [r_i - 1, c_i - 1, r_i, c_i]
    Q = int(input())
    for _ in range(Q):
        d_i, l_i = input().split()
        l_i = int(l_i)
        if d_i == "L":
            c_s = max(c_s - l_i, 1)
        elif d_i == "R":
            c_s = min(c_s + l_i, W)
        elif d_i == "U":
            r_s = max(r_s - l_i, 1)
        elif d_i == "D":
            r_s = min(r_s + l_i, H)
        for i in range(N):
            if r_s == block[i][0] and c_s == block[i][1]:
                if d_i == "L":
                    c_s = min(c_s + l_i, W)
                elif d_i == "R":
                    c_s = max(c_s - l_i, 1)
                elif d_i == "U":
                    r_s = min(r_s + l_i, H)
                elif d_i == "D":
                    r_s = max(r_s - l_i, 1)
        print(r_s, c_s)

if __name__ == '__main__':
    main()