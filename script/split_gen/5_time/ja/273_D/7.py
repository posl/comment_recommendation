def main():
    H, W, r_s, c_s = map(int, input().split())
    N = int(input())
    r_c = []
    for i in range(N):
        r_c.append(list(map(int, input().split())))
    Q = int(input())
    d_l = []
    for i in range(Q):
        d_l.append(list(input().split()))
    #print(H, W, r_s, c_s)
    #print(N)
    #print(r_c)
    #print(Q)
    #print(d_l)
    for i in range(Q):
        now_r = r_s
        now_c = c_s
        for j in range(int(d_l[i][1])):
            if d_l[i][0] == "L":
                now_c -= 1
                if [now_r, now_c] in r_c:
                    now_c += 1
            elif d_l[i][0] == "R":
                now_c += 1
                if [now_r, now_c] in r_c:
                    now_c -= 1
            elif d_l[i][0] == "U":
                now_r -= 1
                if [now_r, now_c] in r_c:
                    now_r += 1
            elif d_l[i][0] == "D":
                now_r += 1
                if [now_r, now_c] in r_c:
                    now_r -= 1
        print(now_r, now_c)
