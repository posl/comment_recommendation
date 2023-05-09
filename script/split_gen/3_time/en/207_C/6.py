def main():
    n = int(input())
    t = []
    l = []
    r = []
    for i in range(n):
        t_i, l_i, r_i = map(int, input().split())
        t.append(t_i)
        l.append(l_i)
        r.append(r_i)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (t[i] == 1 and t[j] == 2) or (t[i] == 2 and t[j] == 1):
                if l[i] <= l[j] and l[j] <= r[i]:
                    count += 1
            elif (t[i] == 1 and t[j] == 3) or (t[i] == 3 and t[j] == 1):
                if l[i] <= l[j] and l[j] < r[i]:
                    count += 1
            elif (t[i] == 1 and t[j] == 4) or (t[i] == 4 and t[j] == 1):
                if l[i] < l[j] and l[j] < r[i]:
                    count += 1
            elif (t[i] == 2 and t[j] == 3) or (t[i] == 3 and t[j] == 2):
                if l[i] < l[j] and l[j] < r[i]:
                    count += 1
            elif (t[i] == 2 and t[j] == 4) or (t[i] == 4 and t[j] == 2):
                if l[i] < l[j] and l[j] <= r[i]:
                    count += 1
            elif (t[i] == 3 and t[j] == 4) or (t[i] == 4 and t[j] == 3):
                if l[i] < l[j] and l[j] < r[i]:
                    count += 1
            else:
                if l[i] <= l[j] and l[j] <= r[i]:
                    count += 1
    print(count)
