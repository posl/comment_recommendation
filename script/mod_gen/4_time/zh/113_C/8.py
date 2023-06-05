def main():
    n,m = map(int,input().split())
    p_y = [list(map(int,input().split())) for _ in range(m)]
    p_y.sort(key=lambda x:(x[0],x[1]))
    p_y_dict = {}
    for i in range(m):
        if p_y[i][0] not in p_y_dict:
            p_y_dict[p_y[i][0]] = 1
        else:
            p_y_dict[p_y[i][0]] += 1
    for i in range(m):
        print(str(p_y[i][0]).zfill(6) + str(p_y_dict[p_y[i][0]]).zfill(6))

if __name__ == '__main__':
    main()