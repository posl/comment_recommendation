def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:x[1])
    p_y_dict = {}
    for i in range(m):
        if p_y[i][0] in p_y_dict:
            p_y_dict[p_y[i][0]] += 1
        else:
            p_y_dict[p_y[i][0]] = 1
    ans = []
    for i in range(m):
        ans.append(str(p_y[i][0]).zfill(6)+str(p_y_dict[p_y[i][0]]).zfill(6))
        p_y_dict[p_y[i][0]] -= 1
    for i in range(m):
        print(ans[i])
main()

if __name__ == '__main__':
    main()