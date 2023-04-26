Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    d, g = map(int, input().split())
    p = [0] * d
    c = [0] * d
    for i in range(d):
        p[i], c[i] = map(int, input().split())
    ans = 1000000000000000000
    for i in range(2 ** d):
        t = 0
        s = 0
        for j in range(d):
            if i >> j & 1:
                t += p[j]
                s += 100 * (j + 1) * p[j] + c[j]
        if g <= s:
            ans = min(ans, t)
        else:
            for j in range(d - 1, -1, -1):
                if i >> j & 1:
                    continue
                for k in range(p[j]):
                    if g <= s:
                        break
                    t += 1
                    s += 100 * (j + 1)
            ans = min(ans, t)
    print(ans)

=======
Suggestion 2

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)

    ans = 1000000000
    for i in range(2**D):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j+1) * p[j] + c[j]
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

=======
Suggestion 3

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)

    ans =

=======
Suggestion 4

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)

    ans = 10000000000000000000
    for i in range(2 ** D):
        sum = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                sum += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j

        if sum < G:
            s1 = 100 * (rest_max + 1)
            need = (G - sum + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    min_num = 1000
    for i in range(2**D):
        num = 0
        score = 0
        for j in range(D):
            if ((i>>j)&1):
                score += (j+1)*100*p[j] + c[j]
                num += p[j]
        if score >= G:
            min_num = min(min_num, num)
        else:
            for j in range(D-1, -1, -1):
                if ((i>>j)&1):
                    continue
                for k in range(p[j]):
                    score += (j+1)*100
                    num += 1
                    if score >= G:
                        min_num = min(min_num, num)
                        break
                break
    print(min_num)

=======
Suggestion 6

def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)

    ans = 10**5
    for i in range(2**d):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(d):
            if ((i >> j) & 1):
                score += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if score < g:
            s1 = 100 * (rest_max + 1)
            need = (g - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    d, g = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(d)]
    ans = float("inf")
    for i in range(2**d):
        count = 0
        total = 0
        rest_max = -1
        for j in range(d):
            if ((i>>j) & 1):
                count += p[j][0]
                total += 100*(j+1)*p[j][0] + p[j][1]
            else:
                rest_max = j
        if total < g:
            s1 = 100*(rest_max+1)
            need = (g-total+s1-1)//s1
            if need >= p[rest_max][0]:
                continue
            count += need
        ans = min(ans, count)
    print(ans)

=======
Suggestion 8

def solve():
    D, G = map(int, input().split())
    p_c = [list(map(int, input().split())) for _ in range(D)]
    ans = 10**9

    for i in range(1 << D):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if i >> j & 1:
                score += 100 * (j + 1) * p_c[j][0] + p_c[j][1]
                cnt += p_c[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= p_c[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 9

def solve():
    # a,b = list(map(int,input().split()))
    # c = list(map(int,input().split()))
    # s = input()
    # h = [list(map(int,input().split())) for i in range(n)]
    # c = list(map(int,input().split()))
    # s = input()
    # h = [list(map(int,input().split())) for i in range(n)]
    d,g = list(map(int,input().split()))
    p = []
    c = []
    for i in range(d):
        a,b = list(map(int,input().split()))
        p.append(a)
        c.append(b)
    ans = 10000000000000
    for i in range(2**d):
        sum = 0
        cnt = 0
        for j in range(d):
            if (i>>j)&1:
                sum += p[j]*(j+1)*100+c[j]
                cnt += p[j]
        if sum >= g:
            ans = min(ans,cnt)
        else:
            for j in range(d-1,-1,-1):
                if (i>>j)&1:
                    continue
                for k in range(p[j]):
                    if sum >= g:
                        break
                    sum += (j+1)*100
                    cnt += 1
            ans = min(ans,cnt)
    print(ans)

=======
Suggestion 10

def get_problem_count(d, g, p, c):
    min_count = 99
