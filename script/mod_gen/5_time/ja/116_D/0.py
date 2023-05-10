def main():
    n,k = map(int,input().split())
    t_d = []
    for i in range(n):
        t,d = map(int,input().split())
        t_d.append([t,d])
    t_d.sort(key=lambda x:x[1],reverse=True)
    #print(t_d)
    t_d_t = t_d[:k]
    #print(t_d_t)
    t_d_t.sort(key=lambda x:x[0])
    #print(t_d_t)
    t_d_t_t = []
    for i in range(len(t_d_t)):
        if t_d_t[i][0] not in t_d_t_t:
            t_d_t_t.append(t_d_t[i][0])
    #print(t_d_t_t)
    #print(len(t_d_t_t))
    t_d_t_t_t = len(t_d_t_t)**2
    #print(t_d_t_t_t)
    t_d_t_t_t_t = 0
    for i in range(len(t_d_t)):
        t_d_t_t_t_t += t_d_t[i][1]
    #print(t_d_t_t_t_t)
    print(t_d_t_t_t_t+t_d_t_t_t_t_t)

if __name__ == '__main__':
    main()