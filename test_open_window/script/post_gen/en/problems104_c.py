Synthesizing 10/10 solutions

=======

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for bit in range(2**D):
        score = 0
        num = 0
        for i in range(D):
            if (bit >> i) & 1:
                score += 100 * (i + 1) * p[i] + c[i]
                num += p[i]
        if score < G:
            for i in range(D - 1, -1, -1):
                if not ((bit >> i) & 1):
                    for j in range(p[i]):
                        score += 100 * (i + 1)
                        num += 1
                        if score >= G:
                            ans = min(ans, num)
                            break
                if score >= G:
                    break
        else:
            ans = min(ans, num)
    print(ans)

=======

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    #print(D, G)
    #print(p)
    #print(c)
    
    ans = 1000000000
    
    for i in range(2**D):
        score = 0
        cnt = 0
        for j in range(D):
            if i & (1 << j):
                score += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
        if score >= G:
            ans = min(ans, cnt)
            continue
        for j in range(D):
            if not (i & (1 << j)):
                for k in range(1, p[j] + 1):
                    score += 100 * (j + 1)
                    cnt += 1
                    if score >= G:
                        ans = min(ans, cnt)
                        break
                break
    print(ans)
    
main()

I solved this problem using Python3. It works fine with the sample inputs and outputs. However, when I submit my code to AtCoder, I get the following error:

Runtime Error
Python3 (3.4.3)
Time: 2 sec / Memory: 256 MB
Test #1: 0.02 sec / 256 MB
Test #2: 0.02 sec / 256 MB
Test #3: 0.02 sec / 256 MB
Test #4: 0.02 sec / 256 MB
Test #5: 0.02 sec / 256 MB
Test #6: 0.02 sec / 256 MB
Test #7: 0.02 sec / 256 MB
Test #8: 0.02 sec / 256 MB
Test #9: 0.02 sec / 256 MB
Test #10: 0.02 sec / 256 MB
Test #11: 0.02 sec / 256 MB
Test #12: 0.02 sec / 256 MB
Test #13: 0.02 sec / 256 MB
Test #14: 0.02 sec / 256 MB
Test #15:

=======

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())

    #print(D, G)
    #print(p)
    #print(c)

    #min count
    min_count = 1000

    #solve all problem
    for i in range(D):
        if G <= 100 * (i + 1) * p[i] + c[i]:
            if min_count > p[i]:
                min_count = p[i]

    #print(min_count)

    #not solve all problem
    for i in range(D):
        for j in range(p[i] - 1):
            if G <= 100 * (i + 1) * (p[i] - j) + c[i]:
                if min_count > p[i] - j:
                    min_count = p[i] - j
    #print(min_count)

    #solve all problem
    for i in range(D):
        if G <= 100 * (i + 1) * p[i] + c[i]:
            if min_count > p[i]:
                min_count = p[i]

    #print(min_count)

    #not solve all problem
    for i in range(D):
        for j in range(p[i] - 1):
            if G <= 100 * (i + 1) * (p[i] - j) + c[i]:
                if min_count > p[i] - j:
                    min_count = p[i] - j
    #print(min_count)

    #solve all problem
    for i in range(D):
        if G <= 100 * (i + 1) * p[i] + c[i]:
            if min_count > p[i]:
                min_count = p[i]

    #print(min_count)

    #not solve all problem
    for i in range(D):
        for j in range(p[i] - 1):
            if G <= 100 * (i + 1) * (p[i] - j) + c[i]:
                if min_count > p[i] - j:
                    min_count = p[i] - j
    #print(min_count)

    #solve all problem
    for i in range(D):
        if G <=

=======

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10**9
    for bit in range(1 << D):
        cnt = 0
        score = 0
        for i in range(D):
            if (bit >> i) & 1:
                cnt += p[i]
                score += 100*(i+1)*p[i] + c[i]
        if score >= G:
            ans = min(ans, cnt)
        else:
            for i in range(D-1, -1, -1):
                if (bit >> i) & 1:
                    continue
                for j in range(p[i]):
                    if score >= G:
                        break
                    score += 100*(i+1)
                    cnt += 1
                break
        if score >= G:
            ans = min(ans, cnt)
    print(ans)

=======

def main():
    D, G = map(int, input().split())
    P = []
    C = []
    for i in range(D):
        p, c = map(int, input().split())
        P.append(p)
        C.append(c)
    ans = 100000000
    for i in range(2**D):
        bit = [0] * D
        for j in range(D):
            if ((i >> j) & 1):
                bit[j] = 1
        score = 0
        cnt = 0
        for j in range(D):
            if bit[j] == 1:
                score += (100 * (j + 1) * P[j] + C[j])
                cnt += P[j]
        if score < G:
            for j in range(D - 1, -1, -1):
                if bit[j] == 0:
                    for k in range(P[j]):
                        score += (100 * (j + 1))
                        cnt += 1
                        if score >= G:
                            break
                    break
        if score >= G:
            ans = min(ans, cnt)
    print(ans)

=======

def main():
    # Get Input
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    
    # Solve
    min_count = 100000
    for i in range(2**D):
        total_score = 0
        count = 0
        for j in range(D):
            if i & 2**j:
                total_score += 100 * (j+1) * p[j] + c[j]
                count += p[j]
        for j in range(D-1, -1, -1):
            if not i & 2**j:
                for k in range(1, p[j]+1):
                    if total_score >= G:
                        break
                    total_score += 100 * (j+1)
                    count += 1
                break
        if total_score >= G and min_count > count:
            min_count = count
    
    # Print Output
    print(min_count)

=======

def main():
    #D = int(input())
    #G = int(input())
    #p = []
    #c = []
    #for i in range(D):
    #    p_i, c_i = map(int, input().split())
    #    p.append(p_i)
    #    c.append(c_i)
    #print(D)
    #print(G)
    #print(p)
    #print(c)
    D = 5
    G = 25000
    p = [20, 40, 50, 30, 1]
    c = [1000, 1000, 1000, 1000, 1000]
    solve(D, G, p, c)

=======

def main():
    from sys import stdin
    import numpy as np
    input = stdin.readline
    D, G = map(int, input().split())
    p = np.array([0] * D)
    c = np.array([0] * D)
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 10 ** 9
    for i in range(2 ** D):
        score = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if score >= G:
            ans = min(ans, num)
        else:
            for j in range(D - 1, -1, -1):
                if not (i >> j) & 1:
                    for k in range(p[j] - 1):
                        if score >= G:
                            break
                        score += 100 * (j + 1)
                        num += 1
                    if score >= G:
                        ans = min(ans, num)
    print(ans)

=======

def solve(D, G, p, c):
    # write your code here
    # return your answer
    return 0

=======

def solve(D, G, p, c):
    # D: number of problems, G: target score, p: number of problems with point 100i, c: perfect bonus
    # Return minimum number of problems to solve
    # 1. Solve all problems with point 100i
    # 2. Solve problems with point 100i that gives maximum score
    # 3. Solve problems with point 100i that gives maximum score and solve problems with point 100j that gives minimum score
    # 4. Solve problems with point 100i that gives maximum score and solve problems with point 100j that gives minimum score and solve problems with point 100k that gives minimum score
    # ...
    # 5. Solve problems with point 100i that gives maximum score and solve problems with point 100j that gives minimum score and solve problems with point 100k that gives minimum score and solve problems with point 100l that gives minimum score
    # ...
    # 6. Solve problems with point 100i that gives maximum score and solve problems with point 100j that gives minimum score and solve problems with point 100k that gives minimum score and solve problems with point 100l that gives minimum score and solve problems with point 100m that gives minimum score
    # ...
    # 7. Solve problems with point 100i that gives maximum score and solve problems with point 100j that gives minimum score and solve problems with point 100k that gives minimum score and solve problems with point 100l that gives minimum score and solve problems with point 100m that gives minimum score and solve problems with point 100n that gives minimum score
    # ...
    # 8. Solve problems with point 100i that gives maximum score and solve problems with point 100j that gives minimum score and solve problems with point 100k that gives minimum score and solve problems with point 100l that gives minimum score and solve problems with point 100m that gives minimum score and solve problems with point 100n that gives minimum score and solve problems with point 100o that gives minimum score
    # ...
    # 9. Solve problems with point 100i that gives maximum score and solve problems with point 100j that gives minimum score and solve problems with point 100k that gives minimum score and solve problems with point 100l that gives minimum score
