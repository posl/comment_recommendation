def main():
    # input
    n, w = map(int, input().split())
    #print(n, w)
    s = []
    t = []
    p = []
    for i in range(n):
        s_i, t_i, p_i = map(int, input().split())
        s.append(s_i)
        t.append(t_i)
        p.append(p_i)
    #print(s, t, p)
    #print('n, w, s, t, p', n, w, s, t, p)
    # process
    # 1. sort s, t, p
    # 2. for each person, check if the water is enough
    # 2.1 if not enough, return No
    # 2.2 if enough, continue
    # 3. return Yes
    #print('n, w, s, t, p', n, w, s, t, p)
    s_sorted, t_sorted, p_sorted = zip(*sorted(zip(s, t, p)))
    #print('n, w, s, t, p', n, w, s, t, p)
    #print('s_sorted, t_sorted, p_sorted', s_sorted, t_sorted, p_sorted)
    #print('n, w, s, t, p', n, w, s, t, p)
    #print('n, w, s, t, p', n, w, s, t, p)
    #print('n, w, s, t, p', n, w, s, t, p)
    #print('n, w, s, t, p', n, w, s, t, p)
    #print('n, w, s, t, p', n, w, s, t, p)
    #print('n, w, s, t, p', n, w, s, t, p)
    #print('n, w, s, t, p', n, w, s, t, p)
    #print('n, w, s, t, p', n, w, s, t, p)
    w_now = w
    for i in range(n):
        s_i = s_sorted[i]
        t_i = t_sorted[i]
        p_i = p_sorted[i]
        #print('w
