def run():
    n,m,q = map(int,input().split())
    l_r = []
    for _ in range(m):
        l_r.append(list(map(int,input().split())))
    p_q = []
    for _ in range(q):
        p_q.append(list(map(int,input().split())))
    for i in range(q):
        count = 0
        for j in range(m):
            if l_r[j][0] >= p_q[i][0] and l_r[j][1] <= p_q[i][1]:
                count += 1
        print(count)

if __name__ == '__main__':
    run()