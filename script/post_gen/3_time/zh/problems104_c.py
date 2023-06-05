Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    D,G = map(int,input().split())
    p = []
    c = []
    for i in range(D):
        p_i,c_i = map(int,input().split())
        p.append(p_i)
        c.append(c_i)
    min_

=======
Suggestion 2

def main():
    D, G = [int(x) for x in input().split()]
    p = []
    c = []
    for i in range(D):
        p_i, c_i = [int(x) for x in input().split()]
        p.append(p_i)
        c.append(c_i)
    min_num = 1000000

=======
Suggestion 3

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for bit in range(1 << D):
        s = 0
        num = 0
        rest_max = -1
        for i in range(D):
            if bit & (1 << i):
                s += 100 * (i + 1) * p[i] + c[i]
                num += p[i]
            else:
                rest_max = i
        if s < G:
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

=======
Suggestion 4

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = 10**9

    for i in range(2**D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
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
Suggestion 5

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 1000
    for i in range(2**D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                s += 100 * (j+1) * p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j
        if s < G:
            s1 = 100 * (rest_max+1)
            need = (G - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 6

def main():
    d, g = map(int, input().split())
    pc = [tuple(map(int, input().split())) for _ in range(d)]

    ans = 10 ** 9
    for i in range(2 ** d):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                s += 100 * (j + 1) * pc[j][0] + pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j

        if s < g:
            s1 = 100 * (rest_max + 1)
            need = (g - s + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 7

def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    ans = 1000
    for i in range(2**d):
        point = 0
        num = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                point += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if point < g:
            s1 = 100 * (rest_max + 1)
            need = (g - point + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

=======
Suggestion 8

def solve():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]

    ans = float('inf')
    for i in range(1 << D):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if i >> j & 1:
                score += 100 * (j + 1) * pc[j][0] + pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j

        if score < G:
            s1 = 100 * (rest_max + 1)
            need = (G - score + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 9

def main():
    D,G = map(int,input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i],c[i] = map(int,input().split())

    ans = 1000000
    for i in range(2**D):
        s = 0
        num = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                s += 100 * (j+1) * p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if s < G:
            s1 = 100 * (rest_max + 1)
            need = (G - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans,num)
    print(ans)

=======
Suggestion 10

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(2**D):
        s = 0
        num = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                s += 100 * (j+1) * p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if s < G:
            s1 = 100 * (rest_max+1)
            need = (G - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)
