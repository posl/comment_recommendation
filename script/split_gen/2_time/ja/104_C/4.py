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
