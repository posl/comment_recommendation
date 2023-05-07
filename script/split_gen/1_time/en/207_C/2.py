def main():
    N = int(input())
    t = []
    l = []
    r = []
    for i in range(N):
        t_i, l_i, r_i = map(int, input().split())
        t.append(t_i)
        l.append(l_i)
        r.append(r_i)
    #print(t)
    #print(l)
    #print(r)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if t[i] == 1 and t[j] == 1:
                if l[i] <= l[j] and l[j] <= r[i]:
                    count += 1
                elif l[j] <= l[i] and l[i] <= r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 2:
                if l[i] <= l[j] and l[j] < r[i]:
                    count += 1
                elif l[j] < l[i] and l[i] <= r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 3:
                if l[i] < l[j] and l[j] <= r[i]:
                    count += 1
                elif l[j] <= l[i] and l[i] < r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 4:
                if l[i] < l[j] and l[j] < r[i]:
                    count += 1
                elif l[j] < l[i] and l[i] < r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 1:
                if l[i] <= l[j] and l[j] <= r[i]:
                    count += 1
                elif l[j] <= l[i] and l[i] <= r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 2:
                if l[i] <= l[j] and l[j] < r[i]:
                    count += 1
                elif l[j] < l[i] and l[i] <= r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 3:
                if l[i] < l[j] and l
