def main():
    a, b, q = map(int, input().split())
    s = [int(input()) for _ in range(a)]
    t = [int(input()) for _ in range(b)]
    x = [int(input()) for _ in range(q)]
    # print(s,t,x)
    for i in range(q):
        tmp = x[i]
        tmp_s = 0
        tmp_t = 0
        for j in range(a):
            if tmp >= s[j]:
                tmp_s = tmp - s[j]
            else:
                tmp_s = s[j] - tmp
            if j == 0:
                min_s = tmp_s
            else:
                if tmp_s < min_s:
                    min_s = tmp_s
        for j in range(b):
            if tmp >= t[j]:
                tmp_t = tmp - t[j]
            else:
                tmp_t = t[j] - tmp
            if j == 0:
                min_t = tmp_t
            else:
                if tmp_t < min_t:
                    min_t = tmp_t
        if min_s < min_t:
            print(min_t)
        else:
            print(min_s)
