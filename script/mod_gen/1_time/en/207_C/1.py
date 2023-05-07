def main():
    N = int(input())
    t = [0] * N
    l = [0] * N
    r = [0] * N
    for i in range(N):
        t[i], l[i], r[i] = map(int, input().split())
    #print(N, t, l, r)
    count = 0
    for i in range(N):
        for j in range(i+1,N):
            if t[i] == 1 and t[j] == 1:
                if l[i] <= l[j] <= r[i] or l[j] <= l[i] <= r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 2:
                if l[i] <= l[j] < r[i] or l[j] < l[i] <= r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 3:
                if l[i] < l[j] <= r[i] or l[j] <= l[i] < r[j]:
                    count += 1
            elif t[i] == 1 and t[j] == 4:
                if l[i] < l[j] < r[i] or l[j] < l[i] < r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 1:
                if l[i] <= l[j] <= r[i] or l[j] <= l[i] <= r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 2:
                if l[i] <= l[j] < r[i] or l[j] < l[i] <= r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 3:
                if l[i] < l[j] <= r[i] or l[j] <= l[i] < r[j]:
                    count += 1
            elif t[i] == 2 and t[j] == 4:
                if l[i] < l[j] < r[i] or l[j] < l[i] < r[j]:
                    count += 1
            elif t[i] == 3 and t[j] == 1:
                if l[i] <= l[j] <= r[i] or

if __name__ == '__main__':
    main()