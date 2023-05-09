def main():
    n,m = map(int, input().split())
    p = []
    y = []
    for i in range(m):
        p_,y_ = map(int, input().split())
        p.append(p_)
        y.append(y_)
    p_y = list(zip(p,y))
    p_y.sort()
    #print(p_y)
    count = 0
    for i in range(m):
        count += 1
        p_y[i] = p_y[i] + (count,)
    #print(p_y)
    p_y.sort(key=lambda x: x[1])
    #print(p_y)
    for i in range(m):
        p_y[i] = p_y[i][0:2]
    #print(p_y)
    for i in range(m):
        p_y[i] = p_y[i] + (str(p_y[i][0]).zfill(6) + str(p_y[i][2]).zfill(6),)
    #print(p_y)
    p_y.sort(key=lambda x: x[2])
    #print(p_y)
    for i in range(m):
        print(p_y[i][2])

if __name__ == '__main__':
    main()