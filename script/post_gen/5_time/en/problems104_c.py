Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    d, g = map(int, input().split())
    p = [0] * d
    c = [0] * d
    for i in range(d):
        p[i], c[i] = map(int, input().split())

    min_count = 1000
    for i in range(2 ** d):
        count = 0
        score = 0
        unsolved_max = -1
        for j in range(d):
            if i >> j & 1:
                count += p[j]
                score += 100 * (j + 1) * p[j] + c[j]
            else:
                unsolved_max = j
        if score < g:
            if unsolved_max != -1:
                rest = (g - score + 100 * (unsolved_max + 1) - 1) // (100 * (unsolved_max + 1))
                if rest < p[unsolved_max]:
                    count += rest
                else:
                    continue
        if min_count > count:
            min_count = count
    print(min_count)

=======
Suggestion 2

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
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
            s1 = 100 * (rest_max+1)
            need = (G - s + s1 - 1) // s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

main()

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
    ans = 1000000000
    for i in range(2**D):
        tmp = 0
        cnt = 0
        for j in range(D):
            if i >> j & 1:
                tmp += c[j] + p[j] * 100 * (j + 1)
                cnt += p[j]
        if tmp >= G:
            ans = min(ans, cnt)
        else:
            for j in range(D - 1, -1, -1):
                if i >> j & 1:
                    continue
                for k in range(p[j]):
                    if tmp >= G:
                        ans = min(ans, cnt)
                        break
                    tmp += 100 * (j + 1)
                    cnt += 1
    print(ans)

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
    min_num = 1000000
    for i in range(2**D):
        num = 0
        score = 0
        for j in range(D):
            if i & (1<<j):
                num += p[j]
                score += 100*(j+1)*p[j] + c[j]
        if score >= G:
            min_num = min(min_num, num)
        else:
            for j in range(D-1, -1, -1):
                if i & (1<<j):
                    continue
                for k in range(p[j]):
                    if score >= G:
                        break
                    num += 1
                    score += 100*(j+1)
            min_num = min(min_num, num)
    print(min_num)

=======
Suggestion 5

def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    min =

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
    ans = float('inf')
    for i in range(2**d):
        s = 0
        num = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
                s += 100*(j+1)*p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if s < g:
            s1 = 100*(rest_max+1)
            need = (g-s+s1-1)//s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

=======
Suggestion 7

def main():
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 10 ** 9
    for i in range(2 ** d):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(d):
            if (i >> j) & 1:
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
Suggestion 8

def solve():
    D, G = map(int, input().split())
    p = []
    c = []
    for _ in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 1e9
    for mask in range(1 << D):
        score = 0
        num = 0
        rest_max = -1
        for i in range(D):
            if (mask >> i) & 1:
                score += 100 * (i + 1) * p[i] + c[i]
                num += p[i]
            else:
                rest_max = i
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

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for i in range(2**D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                cnt += pc[j][0]
                score += 100 * (j+1) * pc[j][0] + pc[j][1]
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
Suggestion 10

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for i in range(1 << D):
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
