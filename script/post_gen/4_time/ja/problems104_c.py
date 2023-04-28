Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    d, g = map(int, input().split())
    p = [0] * d
    c = [0] * d
    for i in range(d):
        p[i], c[i] = map(int, input().split())
    ans = 1000000000000000
    for i in range(2 ** d):
        score = 0
        cnt = 0
        for j in range(d):
            if (i >> j) & 1:
                score += (j + 1) * 100 * p[j] + c[j]
                cnt += p[j]
        if score >= g:
            ans = min(ans, cnt)
        else:
            for j in reversed(range(d)):
                if (i >> j) & 1:
                    continue
                for k in range(p[j]):
                    if score >= g:
                        break
                    score += (j + 1) * 100
                    cnt += 1
            ans = min(ans, cnt)
    print(ans)

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

    ans =

=======
Suggestion 3

def solve():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = float('inf')
    for i in range(2**D):
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

=======
Suggestion 4

def main():
    d,g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)

    result

=======
Suggestion 5

def main():
    d,g = map(int,input().split())
    p = []
    c = []
    for i in range(d):
        p_c = list(map(int,input().split()))
        p.append(p_c[0])
        c.append(p_c[1])
    min_count = 100000000
    for i in range(2**d):
        count = 0
        score = 0
        for j in range(d):
            if (i>>j) & 1 == 1:
                count += p[j]
                score += p[j]*(j+1)*100 + c[j]
        if score >= g:
            min_count = min(min_count,count)
        else:
            for j in range(d-1,-1,-1):
                if (i>>j) & 1 == 0:
                    for k in range(p[j]):
                        if score >= g:
                            break
                        else:
                            score += (j+1)*100
                            count += 1
            min_count = min(min_count,count)
    print(min_count)

=======
Suggestion 6

def main():
    d,g = map(int,input().split())
    p = []
    c = []
    for i in range(d):
        a,b = map(int,input().split())
        p.append(a)
        c.append(b)
    ans = []
    for i in range(1<<d):
        score = 0
        count = 0
        for j in range(d):
            if i&(1<<j):
                score += p[j]*(j+1)*100 + c[j]
                count += p[j]
        if score >= g:
            ans.append(count)
        else:
            for j in range(d-1,-1,-1):
                if i&(1<<j):
                    continue
                for k in range(p[j]):
                    if score >= g:
                        break
                    score += (j+1)*100
                    count += 1
            ans.append(count)
    print(min(ans))

=======
Suggestion 7

def main():
    d, g = map(int, input().split())
    pc = [map(int, input().split()) for _ in range(d)]
    p, c = [list(i) for i in zip(*pc)]

    ans = 10**9
    for i in range(2**d):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(d):
            if ((i >> j) & 1):
                score += 100*(j+1)*p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j

        if score < g:
            s1 = 100*(rest_max+1)
            need = (g - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for i in range(2**D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                s += 100 * (j + 1) * pc[j][0] + pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j
        if s < G:
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 9

def solve():
    D, G = map(int, input().split())
    PC = [list(map(int, input().split())) for _ in range(D)]

    ans = float('inf')
    for i in range(1 << D):
        score = 0
        count = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * PC[j][0] + PC[j][1]
                count += PC[j][0]
            else:
                rest_max = j

        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= PC[rest_max][0]:
                continue
            count += need
        ans = min(ans, count)
    print(ans)

=======
Suggestion 10

def main():
    D, G = map(int, input().split())
    problems = []
    for i in range(D):
        problems.append(list(map(int, input().split())))
    min_num = 100000
    for i in range(2 ** D):
        score = 0
        num = 0
        for j in range(D):
            if ((i >> j) & 1):
                score += (j + 1) * 100 * problems[j][0] + problems[j][1]
                num += problems[j][0]
        if score >= G:
            min_num = min(min_num, num)
        else:
            for j in range(D - 1, -1, -1):
                if ((i >> j) & 1) == 0:
                    for k in range(problems[j][0]):
                        if score >= G:
                            break
                        score += (j + 1) * 100
                        num += 1
            if score >= G:
                min_num = min(min_num, num)
    print(min_num)
