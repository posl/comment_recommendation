Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]

    ans = float('inf')
    for i in range(1 << D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if i >> j & 1:
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
Suggestion 2

def main():
    # D, G = map(int, input().split())
    # P = []
    # C = []
    # for i in range(D):
    #     p, c = map(int, input().split())
    #     P.append(p)
    #     C.append(c)
    D = 5
    G = 25000
    P = [20, 40, 50, 30, 1]
    C = [1000, 1000, 1000, 1000, 1000]
    # print(D, G)
    # print(P)
    # print(C)
    # print(P[0], C[0])
    # print(P[1], C[1])
    # print(P[2], C[2])
    # print(P[3], C[3])
    # print(P[4], C[4])
    # print(P[5], C[5])
    # print(P[6], C[6])
    # print(P[7], C[7])
    # print(P[8], C[8])
    # print(P[9], C[9])
    # print(P[10], C[10])
    # print(P[11], C[11])
    # print(P[12], C[12])
    # print(P[13], C[13])
    # print(P[14], C[14])
    # print(P[15], C[15])
    # print(P[16], C[16])
    # print(P[17], C[17])
    # print(P[18], C[18])
    # print(P[19], C[19])
    # print(P[20], C[20])
    # print(P[21], C[21])
    # print(P[22], C[22])
    # print(P[23], C[23])
    # print(P[24], C[24])
    # print(P[25], C[25])
    # print(P[26], C[26])
    # print(P[27], C[27])
    # print(P[28], C[28])
    # print(P[29], C[29])
    # print(P[30], C[30])
    # print(P[31], C[31])
    # print(P[32], C[32])
    # print(P[

=======
Suggestion 3

def solve():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = 1000
    for i in range(2 ** D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
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
Suggestion 4

def get_min_num_of_problems():
    D, G = map(int, input().split())
    p_c = [list(map(int, input().split())) for i in range(D)]

    min_num_of_problems = 1000
    for i in range(2 ** D):
        num_of_problems = 0
        score = 0
        for j in range(D):
            if i >> j & 1:
                num_of_problems += p_c[j][0]
                score += 100 * (j + 1) * p_c[j][0] + p_c[j][1]
        if score >= G:
            min_num_of_problems = min(min_num_of_problems, num_of_problems)
            continue

        for j in range(D - 1, -1, -1):
            if i >> j & 1:
                continue
            for k in range(p_c[j][0]):
                if score >= G:
                    break
                num_of_problems += 1
                score += 100 * (j + 1)
        min_num_of_problems = min(min_num_of_problems, num_of_problems)
    return min_num_of_problems

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = 10000
    for i in range(2 ** D):
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
Suggestion 7

def main():
    D, G = map(int, input().split())
    pc = []
    for i in range(D):
        p, c = map(int, input().split())
        pc.append([p, c])
    ans = 10000000000
    for i in range(2 ** D):
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
Suggestion 8

def getNumOfProblems(D, G, p, c):
    minNum = 10000
    for i in range(2**D):
        b = bin(i)[2:].zfill(D)
        totalScore = 0
        num = 0
        for j in range(D):
            if b[j] == '1':
                totalScore += p[j] * (j + 1) * 100 + c[j]
                num += p[j]
        for j in range(D - 1, -1, -1):
            if b[j] == '0':
                if totalScore < G:
                    if totalScore + p[j] * (j + 1) * 100 >= G:
                        num += (G - totalScore) // ((j + 1) * 100)
                break
        if totalScore >= G and num < minNum:
            minNum = num
    return minNum

=======
Suggestion 9

def main():
    d,g=map(int,input().split())
    p=[]
    c=[]
    for i in range(d):
        p1,c1=map(int,input().split())
        p.append(p1)
        c.append(c1)
    ans=1000000
    for i in range(2**d):
        cnt=0
        score=0
        rest_max=-1
        for j in range(d):
            if ((i>>j)&1):
                score+=100*(j+1)*p[j]+c[j]
                cnt+=p[j]
            else:
                rest_max=j
        if score<g:
            s=(g-score+100*(rest_max+1)-1)//(100*(rest_max+1))
            if s>=p[rest_max]:
                continue
            cnt+=s
        ans=min(ans,cnt)
    print(ans)

=======
Suggestion 10

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        a, b = map(int, input().split())
        p.append(a)
        c.append(b)
    ans = 10000000
    for i in range(1 << D):
        s = 0
        num = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                s += 100 * (j + 1) * p[j] + c[j]
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
