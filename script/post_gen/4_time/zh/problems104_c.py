Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # 读取输入
    d, g = map(int, input().split())
    p = []
    c = []
    for i in range(d):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)

    # 算法
    ans =

=======
Suggestion 2

def get_input():
    input_list = []
    while True:
        try:
            input_list.append(input())
        except EOFError:
            break
    return input_list

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
    ans = 10000000
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
Suggestion 4

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


solve()

=======
Suggestion 5

def solve():
    D,G = map(int,input().split())
    pc = [list(map(int,input().split())) for _ in range(D)]
    ans = float("inf")
    for i in range(2**D):
        s = 0
        cnt = 0
        rest_max = -1
        for j in range(D):
            if ((i>>j) & 1):
                s += 100*(j+1)*pc[j][0] + pc[j][1]
                cnt += pc[j][0]
            else:
                rest_max = j
        if s < G:
            s1 = 100*(rest_max+1)
            need = (G-s+s1-1)//s1
            if need >= pc[rest_max][0]:
                continue
            cnt += need
        ans = min(ans,cnt)
    print(ans)

solve()

=======
Suggestion 6

def main():
    D,G = map(int,input().split())
    pc = [list(map(int,input().split())) for _ in range(D)]
    ans = 10**9
    for i in range(2**D):
        count = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
                score += 100 * (j+1) * pc[j][0] + pc[j][1]
                count += pc[j][0]
            else:
                rest_max = j
        if score < G:
            s1 = 100 * (rest_max+1)
            need = (G - score + s1 - 1) // s1
            if need >= pc[rest_max][0]:
                continue
            count += need
        ans = min(ans,count)
    print(ans)

=======
Suggestion 7

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]
    ans = float('inf')
    for i in range(2**D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if (i >> j) & 1:
                score += pc[j][0] * 100 * (j + 1) + pc[j][1]
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
Suggestion 8

def main():
    pass

=======
Suggestion 9

def main():
    D,G = map(int,input().split())
    p = []
    c = []
    for i in range(D):
        p_tmp,c_tmp = map(int,input().split())
        p.append(p_tmp)
        c.append(c_tmp)
    ans = 1000000000
    for i in range(2**D):
        cnt = 0
        score = 0
        rest_max = -1
        for j in range(D):
            if ((i >> j) & 1):
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
        ans = min(ans,cnt)
    print(ans)

=======
Suggestion 10

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())

    ans = 1000000000000000
    for i in range(2 ** D):
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
