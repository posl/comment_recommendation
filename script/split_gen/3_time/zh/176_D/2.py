def main():
    h,w = map(int, input().split())
    c_h,c_w = map(int, input().split())
    d_h,d_w = map(int, input().split())
    c_h -= 1
    c_w -= 1
    d_h -= 1
    d_w -= 1
    s = []
    for i in range(h):
        s.append(input())
    # print(s)
    ans = [[-1 for i in range(w)] for j in range(h)]
    ans[c_h][c_w] = 0
    # print(ans)
    q = [[c_h,c_w]]
    while len(q) > 0:
        # print(q)
        h,w = q.pop(0)
        # print(h,w)
        for i in range(-2,3):
            for j in range(-2,3):
                if abs(i) + abs(j) == 4:
                    continue
                if h+i < 0 or h+i >= len(s) or w+j < 0 or w+j >= len(s[0]):
                    continue
                if s[h+i][w+j] == '#':
                    continue
                if ans[h+i][w+j] == -1:
                    ans[h+i][w+j] = ans[h][w] + 1
                    q.append([h+i,w+j])
    print(ans[d_h][d_w])
main()
