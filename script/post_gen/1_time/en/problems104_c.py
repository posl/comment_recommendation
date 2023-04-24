Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    D, G = map(int, input().split())
    P = []
    C = []
    for i in range(D):
        p, c = map(int, input().split())
        P.append(p)
        C.append(c)
    ans =

=======
Suggestion 2

def main():
    D, G = map(int, input().split())
    P = []
    C = []
    for i in range(D):
        p, c = map(int, input().split())
        P.append(p)
        C.append(c)
    min_count = 10**9
    for i in range(2**D):
        count = 0
        score = 0
        for j in range(D):
            if i >> j & 1:
                count += P[j]
                score += 100 * (j+1) * P[j] + C[j]
        if score >= G:
            min_count = min(min_count, count)
        else:
            for j in range(D-1, -1, -1):
                if not i >> j & 1:
                    for k in range(P[j]):
                        if score >= G:
                            break
                        else:
                            score += 100 * (j+1)
                            count += 1
            min_count = min(min_count, count)
    print(min_count)

=======
Suggestion 3

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    min_count = 10**9
    for i in range(2**D):
        count = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j + 1) * p[j] + c[j]
                count += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            count += need
        min_count = min(min_count, count)
    print(min_count)

=======
Suggestion 4

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = float("inf")
    for i in range(2 ** D):
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
Suggestion 5

def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        a, b = map(int, input().split())
        p.append(a)
        c.append(b)
    ans = 10 ** 10
    for i in range(1 << d):
        count = 0
        score = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                count += p[j]
            else:
                rest_max = j
        if score < g:
            s1 = 100 * (rest_max + 1)
            need = (g - score + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            count += need
        ans = min(ans, count)
    print(ans)

=======
Suggestion 6

def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p1, c1 = map(int, input().split())
        p.append(p1)
        c.append(c1)
    ans = float("inf")
    for i in range(2**d):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(d):
            if ((i>>j) & 1):
                score += 100*(j+1)*p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if score < g:
            s1 = 100*(rest_max+1)
            need = (g - score + s1 - 1)//s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    D, G = map(int, input().split())
    p = [0] * (D + 1)
    c = [0] * (D + 1)
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10 ** 9
    for i in range(2 ** D):
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
Suggestion 8

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = 10**9
    for i in range(2**D):
        cnt = 0
        tmp = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                cnt += pc[j][0]
                tmp += 100 * (j + 1) * pc[j][0] + pc[j][1]
            else:
                rest_max = j
        if tmp < G:
            s1 = 100 * (rest_max + 1)
            need = (G - tmp + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 9

def main():
    D, G = map(int, input().split())
    PC = []
    for i in range(D):
        p, c = map(int, input().split())
        PC.append((p, c))
    print(solve(D, G, PC))

=======
Suggestion 10

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = 1000000000000000000
    for i in range(2**D):
        sum = 0
        num = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                sum += pc[j][0] * (j+1) * 100 + pc[j][1]
                num += pc[j][0]
            else:
                rest_max = j
        if sum < G:
            s1 = (rest_max + 1) * 100
            need = (G - sum + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)
