Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    d,g = map(int,input().split())
    p = []
    c = []
    for i in range(d):
        p_i,c_i = map(int,input().split())
        p.append(p_i)
        c.append(c_i)

=======
Suggestion 2

def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)

    ans = 1000000000
    for i in range(2**d):
        point = 0
        num = 0
        rest_max = -1
        for j in range(d):
            if ((i >> j) & 1):
                point += 100 * (j+1) * p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if point < g:
            s1 = 100 * (rest_max+1)
            need = (g - point + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

=======
Suggestion 3

def main():
    # D, G = map(int, input().split())
    # p, c = zip(*[map(int, input().split()) for _ in range(D)])
    # ans = 10 ** 9
    # for i in range(1 << D):
    #     s = 0
    #     cnt = 0
    #     rest_max = -1
    #     for j in range(D):
    #         if (i >> j) & 1:
    #             s += 100 * (j + 1) * p[j] + c[j]
    #             cnt += p[j]
    #         else:
    #             rest_max = j
    #     if s < G:
    #         s1 = 100 * (rest_max + 1)
    #         need = (G - s + s1 - 1) // s1
    #         if need >= p[rest_max]:
    #             continue
    #         cnt += need
    #     ans = min(ans, cnt)
    # print(ans)
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    ans = 10 ** 9
    for i in range(1 << D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                s += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if s < G:
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    n, g = map(int, input().split())
    p = [0]
    c = [0]
    for i in range(n):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    ans = 10**10
    for i in range(2**n):
        point = 0
        count = 0
        rest_max = -1
        for j in range(n):
            if (i >> j) & 1:
                point += p[j + 1] * 100 * (j + 1) + c[j + 1]
                count += p[j + 1]
            else:
                rest_max = j + 1
        if point < g:
            s1 = (g - point + 100 * rest_max - 1) // (100 * rest_max)
            if s1 < p[rest_max]:
                count += s1
            else:
                continue
        ans = min(ans, count)
    print(ans)
main()

=======
Suggestion 5

def main():
    d,g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    
    ans = 10000000000
    for i in range(2**d):
        score = 0
        num = 0
        for j in range(d):
            if (i >> j) & 1:
                score += p[j] * 100 * (j+1) + c[j]
                num += p[j]
        if score >= g:
            ans = min(ans, num)
            continue
        for j in range(d-1, -1, -1):
            if (i >> j) & 1:
                continue
            for k in range(p[j]):
                if score >= g:
                    break
                score += 100 * (j+1)
                num += 1
        ans = min(ans, num)
    print(ans)

=======
Suggestion 6

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 10**9
    for i in range(1 << D):
        score = 0
        num = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

=======
Suggestion 7

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = float("inf")
    for i in range(2 ** D):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)
main()

=======
Suggestion 8

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10 ** 9
    for i in range(2 ** D):
        num = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

=======
Suggestion 9

def solve():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for i in range(2**D):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += 100*(j+1)*pc[j][0] + pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100*(rest_max+1)
            need = (G-score+s1-1)//s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

solve()

=======
Suggestion 10

def solve():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]

    ans = float('inf')
    for i in range(1<<D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if i >> j & 1:
                score += 100 * (j+1) * pc[j][0] + pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max+1)
            need = (G - score + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

solve()
