def main():
    n_q = list(map(int, input().split()))
    n = n_q[0]
    q = n_q[1]
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    s_t = []
    for j in range(q):
        s_t.append(list(map(int, input().split())))
    for k in range(q):
        print(a[s_t[k][0]-1][s_t[k][1]-1])

if __name__ == '__main__':
    main()