Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(2**D):
        score = 0
        count = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                count += p[j]
        if score >= G:
            ans = min(ans, count)
        else:
            for j in range(D - 1, -1, -1):
                if (i >> j) & 1 == 0:
                    for k in range(p[j] - 1):
                        score += 100 * (j + 1)
                        count += 1
                        if score >= G:
                            ans = min(ans, count)
                    break
    print(ans)

=======
Suggestion 2

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for i in range(1 << D):
        score = 0
        cnt = 0
        for j in range(D):
            if i & (1 << j):
                score += 100 * (j+1) * p[j] + c[j]
                cnt += p[j]
        if score < G:
            for j in range(D-1, -1, -1):
                if not(i & (1 << j)):
                    for k in range(p[j]):
                        if score >= G:
                            break
                        score += 100 * (j+1)
                        cnt += 1
                    break
        if score >= G:
            ans = min(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for bit in range(1<<D):
        score = 0
        cnt = 0
        for i in range(D):
            if bit & (1<<i):
                score += 100 * (i+1) * p[i] + c[i]
                cnt += p[i]
        if score < G:
            for i in range(D-1, -1, -1):
                if bit & (1<<i):
                    continue
                for j in range(p[i]):
                    if score >= G:
                        break
                    score += 100 * (i+1)
                    cnt += 1
                break
        if score >= G:
            ans = min(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10 ** 9
    for i in range(2 ** D):
        s = 0
        cnt = 0
        for j in range(D):
            if ((i >> j) & 1):
                s += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
        if s >= G:
            ans = min(ans, cnt)
            continue
        for j in range(D - 1, -1, -1):
            if ((i >> j) & 1):
                continue
            for k in range(p[j]):
                if s >= G:
                    break
                s += 100 * (j + 1)
                cnt += 1
            if s >= G:
                break
        if s >= G:
            ans = min(ans, cnt)
    print(ans)

=======
Suggestion 5

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())

    # 2^D通りの解法を全探索
    ans = 10**9
    for bit in range(1 << D):
        score = 0
        num = 0
        for i in range(D):
            if bit & (1 << i):
                # 問題を解く
                score += 100 * (i + 1) * p[i] + c[i]
                num += p[i]
        if score < G:
            # 解いた問題の中で1番難しいものを解く
            for i in range(D - 1, -1, -1):
                if bit & (1 << i):
                    continue
                for j in range(p[i]):
                    score += 100 * (i + 1)
                    num += 1
                    if score >= G:
                        break
                if score >= G:
                    break
        if score >= G:
            ans = min(ans, num)

    print(ans)

=======
Suggestion 6

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    
    ans = 1000000000
    for i in range(2**D):
        cnt = 0
        score = 0
        for j in range(D):
            if (i >> j) & 1:
                cnt += p[j]
                score += 100 * (j + 1) * p[j] + c[j]
        
        if score >= G:
            ans = min(ans, cnt)
            continue
        
        for j in range(D - 1, -1, -1):
            if (i >> j) & 1:
                continue
            
            for k in range(p[j]):
                cnt += 1
                score += 100 * (j + 1)
                
                if score >= G:
                    ans = min(ans, cnt)
                    break
            
            break
    
    print(ans)

=======
Suggestion 7

def main():
    D, G = map(int, input().split())
    p = []
    c = []
    for i in range(D):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = 10**9
    for i in range(1<<D):
        score = 0
        num = 0
        for j in range(D):
            if (i>>j) & 1:
                score += 100*(j+1)*p[j] + c[j]
                num += p[j]
        if score >= G:
            ans = min(ans, num)
        else:
            for j in range(D-1, -1, -1):
                if (i>>j) & 1:
                    continue
                for k in range(p[j]):
                    score += 100*(j+1)
                    num += 1
                    if score >= G:
                        ans = min(ans, num)
                        break
                break
    print(ans)

=======
Suggestion 8

def main():
    D, G = list(map(int, input().split()))
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = list(map(int, input().split()))
    #print(D, G)
    #print(p)
    #print(c)
    #print("")

    min_count = 10000
    for i in range(2**D):
        score = 0
        count = 0
        for j in range(D):
            if i & (1 << j):
                score += (j+1) * 100 * p[j] + c[j]
                count += p[j]
        if score >= G:
            if count < min_count:
                min_count = count
        else:
            for j in range(D-1, -1, -1):
                if not i & (1 << j):
                    for k in range(p[j]-1):
                        score += (j+1) * 100
                        count += 1
                        if score >= G:
                            if count < min_count:
                                min_count = count
                    break
    print(min_count)

=======
Suggestion 9

def main():
    import sys
    f = open('input.txt', 'r')
    D, G = map(int, f.readline().split())
    p = []
    c = []
    for i in range(D):
        pi, ci = map(int, f.readline().split())
        p.append(pi)
        c.append(ci)
    f.close()

    #print(D)
    #print(G)
    #print(p)
    #print(c)

    #print(p[0])

    #print(p[0]*100)
    #print(p[0]*100 + c[0])

    #print(p[1]*200)
    #print(p[1]*200 + c[1])

    #print(p[2]*300)
    #print(p[2]*300 + c[2])

    #print(p[3]*400)
    #print(p[3]*400 + c[3])

    #print(p[4]*500)
    #print(p[4]*500 + c[4])

    #print(p[5]*600)
    #print(p[5]*600 + c[5])

    #print(p[6]*700)
    #print(p[6]*700 + c[6])

    #print(p[7]*800)
    #print(p[7]*800 + c[7])

    #print(p[8]*900)
    #print(p[8]*900 + c[8])

    #print(p[9]*1000)
    #print(p[9]*1000 + c[9])

    #print(p[10]*1100)
    #print(p[10]*1100 + c[10])

    #print(p[11]*1200)
    #print(p[11]*1200 + c[11])

    #print(p[12]*1300)
    #print(p[12]*1300 + c[12])

    #print(p[13]*1400)
    #print(p[13]*1400 + c[13])

    #print(p[14]*1500)
    #print(p[14]*1500 + c[14])

    #print(p[15]*1600)
    #print(p[15]*1600 + c[15])

    #print(p[16]*1700)
    #print(p[16]*1700 + c[16])

    #print(p[17]*1800)

=======
Suggestion 10

def read_int():
    return int(input())
