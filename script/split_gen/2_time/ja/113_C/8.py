def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:x[1])
    p_y_dict = {}
    for p, y in p_y:
        if p in p_y_dict:
            p_y_dict[p].append(y)
        else:
            p_y_dict[p] = [y]
    ans = []
    for p, y in p_y:
        ans.append(str(p).zfill(6) + str(p_y_dict[p].index(y) + 1).zfill(6))
    print(*ans, sep='\n')
