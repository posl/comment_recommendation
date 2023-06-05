def problem113_c():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:x[1])
    p_y_dict = {}
    for p, y in p_y:
        if p not in p_y_dict:
            p_y_dict[p] = 1
        else:
            p_y_dict[p] += 1
    ans = {}
    for p, y in p_y:
        ans[y] = str(p).zfill(6) + str(p_y_dict[p]).zfill(6)
        p_y_dict[p] -= 1
    for y in p_y:
        print(ans[y[1]])
