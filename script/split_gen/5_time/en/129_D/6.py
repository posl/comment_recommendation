def main():
    h, w = map(int, input().split())
    s = []
    for _ in range(h):
        s.append(input())
    # print(s)
    w_list = []
    for i in range(h):
        w_list.append(s[i].count('.'))
    # print(w_list)
    h_list = []
    for i in range(w):
        tmp = 0
        for j in range(h):
            if s[j][i] == '.':
                tmp += 1
        h_list.append(tmp)
    # print(h_list)
    ans = 0
    for i in range(h):
        for j in range(w):
            if s[i][j] == '.':
                tmp = w_list[i] + h_list[j] - 1
            else:
                tmp = w_list[i] + h_list[j]
            if ans < tmp:
                ans = tmp
    print(ans)
