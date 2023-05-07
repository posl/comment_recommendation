def main():
    N = int(input())
    q = []
    for _ in range(N):
        q.append(list(map(int, input().split())))
    l = []
    r = []
    lsum = 0
    rsum = 0
    for i in range(N):
        if q[i][0] == 1:
            r.append(q[i][1])
            rsum += q[i][1] * q[i][2]
        else:
            if q[i][1] > len(l):
                q[i][1] -= len(l)
                l = []
                lsum = 0
                if q[i][1] > len(r):
                    r = []
                    rsum = 0
                else:
                    r = r[q[i][1]:]
                    rsum = sum(r)
            else:
                l = l[q[i][1]:]
                lsum = sum(l)
        if q[i][0] == 2:
            print(lsum + rsum)
