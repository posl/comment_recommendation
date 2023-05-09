def main():
    n, m = map(int, input().split())
    p_y = [list(map(int, input().split())) for _ in range(m)]
    p_y = sorted(p_y, key=lambda x: x[1])
    p_y_dict = {}
    for p, y in p_y:
        if p not in p_y_dict:
            p_y_dict[p] = 1
        else:
            p_y_dict[p] += 1
    ans = []
    for p, y in p_y:
        ans.append('{0:06d}{1:06d}'.format(p, p_y_dict[p]))
        p_y_dict[p] += 1
    print(*ans, sep='\n')

if __name__ == '__main__':
    main()