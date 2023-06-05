def problem214_c():
    n = int(input())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    # print(n)
    # print(s)
    # print(t)
    res = [0] * n
    for i in range(n):
        res[i] = t[i]
    for i in range(n):
        if i == 0:
            if s[i] < t[i]:
                res[i] = s[i]
        else:
            if s[i] < t[i]:
                res[i] = s[i]
            else:
                if res[i-1] + s[i-1] < t[i]:
                    res[i] = res[i-1] + s[i-1]
                else:
                    res[i] = t[i]
    for i in range(n):
        print(res[i])

if __name__ == '__main__':
    problem214_c()