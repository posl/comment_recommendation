def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y = sorted(p_y, key=lambda x: x[1])
    p_y = sorted(p_y, key=lambda x: x[0])
    #print(p_y)
    p_y_s = []
    for i in range(len(p_y)):
        p_y_s.append([p_y[i][0], p_y[i][1], i+1])
    #print(p_y_s)
    p_y_s = sorted(p_y_s, key=lambda x: x[1])
    #print(p_y_s)
    ans = []
    for i in range(len(p_y_s)):
        ans.append([p_y_s[i][0], p_y_s[i][2]])
    #print(ans)
    ans = sorted(ans, key=lambda x: x[0])
    #print(ans)
    for i in range(len(ans)):
        print('{:06}{:06}'.format(ans[i][0], ans[i][1]))

if __name__ == '__main__':
    main()