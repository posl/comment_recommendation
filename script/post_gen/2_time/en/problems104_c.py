Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10000
    for i in range(2 ** D):
        score = 0
        cnt = 0
        for j in range(D):
            if i & (1 << j):
                score += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
        if score < G:
            for j in range(D - 1, -1, -1):
                if not (i & (1 << j)):
                    for k in range(p[j]):
                        score += 100 * (j + 1)
                        cnt += 1
                        if score >= G:
                            ans = min(ans, cnt)
                            break
                    break
        else:
            ans = min(ans, cnt)
    print(ans)

=======
Suggestion 2

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #print(p)
    #print(c)
    #print(D, G)
    #print(p)
    #print(c)
    #print("-----")
    min = 1000000
    for i in range(1, 2**D):
        #print("i",i)
        sum = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                sum += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        #print("sum",sum)
        #print("num",num)
        if sum >= G:
            if num < min:
                min = num
        else:
            for j in range(D):
                if not ((i >> j) & 1):
                    for k in range(p[j]):
                        sum += 100 * (j + 1)
                        num += 1
                        if sum >= G:
                            if num < min:
                                min = num
                            break
                    break
        #print("sum",sum)
        #print("num",num)
        #print("-----")
    print(min)

=======
Suggestion 3

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(2**D):
        tmp = 0
        score = 0
        for j in range(D):
            if (i >> j) & 1:
                tmp += p[j]
                score += 100 * (j+1) * p[j] + c[j]
        if score >= G:
            ans = min(ans, tmp)
        else:
            for j in range(D-1, -1, -1):
                if (i >> j) & 1:
                    continue
                for k in range(p[j]):
                    if score >= G:
                        break
                    score += 100 * (j+1)
                    tmp += 1
                break
            if score >= G:
                ans = min(ans, tmp)
    print(ans)

=======
Suggestion 4

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 1000000000
    for i in range(2 ** D):
        sum = 0
        num = 0
        max_num = 0
        for j in range(D):
            if (i >> j) & 1:
                sum += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
            else:
                max_num = j
        if sum < G:
            k = G - sum
            if k > 100 * (max_num + 1) * p[max_num]:
                continue
            else:
                num += -(-k // (100 * (max_num + 1)))
        ans = min(ans, num)
    print(ans)

=======
Suggestion 5

def main():
    D, G = map(int, input().split())
    p = [0 for i in range(D)]
    c = [0 for i in range(D)]
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #print(p)
    #print(c)
    ans =

=======
Suggestion 6

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        tmp = list(map(int, input().split()))
        p.append(tmp[0])
        c.append(tmp[1])
    ans = 100000
    for i in range(2**D):
        tmp = 0
        cnt = 0
        for j in range(D):
            if (i >> j) & 1:
                tmp += 100*(j+1)*p[j] + c[j]
                cnt += p[j]
        if tmp >= G:
            ans = min(ans, cnt)
            continue
        for j in range(D-1, -1, -1):
            if (i >> j) & 1:
                continue
            for k in range(p[j]):
                if tmp >= G:
                    break
                tmp += 100*(j+1)
                cnt += 1
            if tmp >= G:
                ans = min(ans, cnt)
                break
    print(ans)

=======
Suggestion 7

def main():
    #input
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #compute
    ans = 10**9
    for i in range(2**D):
        score = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if score < G:
            for j in range(D):
                if not (i >> (D - 1 - j)) & 1:
                    for k in range(p[D - 1 - j]):
                        if score >= G:
                            break
                        score += 100 * (D - j)
                        num += 1
        if score >= G:
            ans = min(ans, num)
    #output
    print(ans)

=======
Suggestion 8

def main():
    #input
    D, G = map(int, input().split())
    p = [0 for i in range(D)]
    c = [0 for i in range(D)]
    for i in range(D):
        p[i], c[i] = map(int, input().split())

    #calc
    ans = 10**10
    for i in range(2**D):
        cnt = 0
        score = 0
        for j in range(D):
            if (i >> j) & 1 == 1:
                cnt += p[j]
                score += (j+1)*100*p[j] + c[j]
        if score >= G:
            ans = min(ans, cnt)
        else:
            for j in range(D-1, -1, -1):
                if (i >> j) & 1 == 0:
                    for k in range(p[j]):
                        if score >= G:
                            break
                        score += (j+1)*100
                        cnt += 1
                    if score >= G:
                        ans = min(ans, cnt)
                    break

    #output
    print(ans)

=======
Suggestion 9

def solve(D, G, p, c):
    # Write your code here
    pass
