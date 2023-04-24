Synthesizing 10/10 solutions

=======
Suggestion 1

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
Suggestion 2

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10000
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
        ans = min(ans, num)
    print(ans)

=======
Suggestion 3

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())

    ans = float('inf')
    for i in range(1 << D):
        score = 0
        count = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
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
        ans = min(ans, count)
    print(ans)

=======
Suggestion 4

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)

    ans = 10**9
    for i in range(2**D):
        count = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += 100*(j+1)*p[j] + c[j]
                count += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100*(rest_max+1)
            need = (G-score+s1-1)//s1
            if need >= p[rest_max]:
                continue
            count += need
        ans = min(ans, count)
    print(ans)

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

    min_problem = 100000
    for i in range(2**d):
        problem = 0
        score = 0
        for j in range(d):
            if i & (1 << j):
                problem += p[j]
                score += (j+1)*100*p[j] + c[j]
        if score >= g:
            min_problem = min(min_problem, problem)
        else:
            for j in range(d-1, -1, -1):
                if i & (1 << j):
                    continue
                for k in range(p[j]):
                    if score >= g:
                        break
                    problem += 1
                    score += (j+1)*100
            min_problem = min(min_problem, problem)
    print(min_problem)

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

    ans = 10000
    for i in range(2**d):
        score = 0
        cnt = 0
        rest_max = -1
        for j in range(d):
            if ((i >> j) & 1):
                score += 100*(j+1)*p[j] + c[j]
                cnt += p[j]
            else:
                rest_max = j

        if score < g:
            s1 = 100*(rest_max+1)
            need = (g-score+s1-1)//s1
            if need >= p[rest_max]:
                continue
            cnt += need
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 7

def solve():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int, input().split())
        p.append(pi)
        c.append(ci)
    ans = 10**10
    for i in range(1<<D):
        #print(i)
        score = 0
        num = 0
        rest_max = -1
        for j in range(D):
            if (i>>j)&1:
                score += 100*(j+1)*p[j] + c[j]
                num += p[j]
            else:
                rest_max = j
        if score < G:
            s1 = 100*(rest_max+1)
            need = (G-score+s1-1)//s1
            if need >= p[rest_max]:
                continue
            num += need
        ans = min(ans, num)
    print(ans)

solve()

=======
Suggestion 8

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        a, b = map(int, input().split())
        p.append(a)
        c.append(b)

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

=======
Suggestion 9

def main():
    d,g = map(int,input().split())
    p = [0]*d
    c = [0]*d
    for i in range(d):
        p[i],c[i] = map(int,input().split())

=======
Suggestion 10

def main():
    D,G=map(int,input().split())
    p=[]
    c=[]
    for i in range(D):
        p1,c1=map(int,input().split())
        p.append(p1)
        c.append(c1)
    ans=10**9
    for i in range(2**D):
        s=0
        cnt=0
        rest_max=-1
        for j in range(D):
            if (i>>j)&1:
                s+=100*(j+1)*p[j]+c[j]
                cnt+=p[j]
            else:
                rest_max=j
        if s<G:
            s1=100*(rest_max+1)
            need=(G-s+s1-1)//s1
            if need>=p[rest_max]:
                continue
            cnt+=need
        ans=min(ans,cnt)
    print(ans)
