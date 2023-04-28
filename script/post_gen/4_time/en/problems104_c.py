Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    ans = 100000000000000
    for i in range(2 ** D):
        score = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                score += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if score >= G:
            ans = min(ans, num)
            continue
        for j in range(D - 1, -1, -1):
            if (i >> j) & 1:
                continue
            for k in range(p[j]):
                score += 100 * (j + 1)
                num += 1
                if score >= G:
                    ans = min(ans, num)
                    break
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
    ans = 10 ** 10
    for i in range(2 ** D):
        sum = 0
        num = 0
        for j in range(D):
            if i >> j & 1:
                sum += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if sum < G:
            for j in range(D - 1, -1, -1):
                if not i >> j & 1:
                    for k in range(p[j]):
                        sum += 100 * (j + 1)
                        num += 1
                        if sum >= G:
                            ans = min(ans, num)
                            break
                    break
        else:
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
    ans = 10**9
    for i in range(1, 1 << D):
        tmp = 0
        cnt = 0
        for j in range(D):
            if i & (1 << j):
                tmp += (j + 1) * 100 * p[j] + c[j]
                cnt += p[j]
        if tmp < G:
            for j in range(D - 1, -1, -1):
                if not i & (1 << j):
                    for k in range(p[j]):
                        if tmp >= G:
                            break
                        tmp += (j + 1) * 100
                        cnt += 1
                    break
        if tmp >= G:
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
    ans = 10**9
    for bit in range(2**D):
        cnt = 0
        score = 0
        for i in range(D):
            if bit & (1 << i):
                cnt += p[i]
                score += 100 * (i + 1) * p[i] + c[i]
        if score >= G:
            ans = min(ans, cnt)
        else:
            for i in range(D - 1, -1, -1):
                if bit & (1 << i):
                    continue
                for j in range(p[i]):
                    cnt += 1
                    score += 100 * (i + 1)
                    if score >= G:
                        ans = min(ans, cnt)
                        break
                break
    print(ans)

=======
Suggestion 5

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    min_num = 100 * D
    for i in range(2**D):
        total = 0
        num = 0
        for j in range(D):
            if (i >> j) & 1:
                total += 100 * (j + 1) * p[j] + c[j]
                num += p[j]
        if total >= G:
            min_num = min(min_num, num)
        else:
            for j in range(D - 1, -1, -1):
                if not((i >> j) & 1):
                    for k in range(p[j]):
                        total += 100 * (j + 1)
                        num += 1
                        if total >= G:
                            min_num = min(min_num, num)
                            break
                    break
    print(min_num)

=======
Suggestion 6

def main():
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    
    ans = 10**9
    for bit in range(1 << D):
        score = 0
        cnt = 0
        for i in range(D):
            if bit & (1 << i):
                score += 100 * (i + 1) * p[i] + c[i]
                cnt += p[i]
        if score >= G:
            ans = min(ans, cnt)
            continue
        for i in range(D - 1, -1, -1):
            if bit & (1 << i):
                continue
            for j in range(p[i]):
                score += 100 * (i + 1)
                cnt += 1
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

    ans = 1000000000
    for i in range(2**D):
        cnt = 0
        score = 0
        for j in range(D):
            if i >> j & 1:
                cnt += p[j]
                score += p[j]*(j+1)*100 + c[j]
        if score >= G:
            ans = min(ans, cnt)
        else:
            for j in range(D-1, -1, -1):
                if not i >> j & 1:
                    for k in range(p[j]):
                        if score >= G:
                            break
                        score += (j+1)*100
                        cnt += 1
                    break
        if score >= G:
            ans = min(ans, cnt)

    print(ans)

=======
Suggestion 8

def main():
    # Read input
    D, G = map(int, input().split())
    p = [0] * D
    c = [0] * D
    for i in range(D):
        p[i], c[i] = map(int, input().split())
    
    # Solve
    ans = 10 ** 9
    for i in range(2 ** D):
        cnt = 0
        score = 0
        for j in range(D):
            if i & (1 << j):
                cnt += p[j]
                score += 100 * (j + 1) * p[j] + c[j]
        if score >= G:
            ans = min(ans, cnt)
        else:
            for j in range(D - 1, -1, -1):
                if not i & (1 << j):
                    for k in range(p[j]):
                        cnt += 1
                        score += 100 * (j + 1)
                        if score >= G:
                            ans = min(ans, cnt)
                        if score >= G:
                            break
                    break
    print(ans)

main()

=======
Suggestion 9

def main():
    D, G = map(int, input().split())
    pc = [list(map(int, input().split())) for _ in range(D)]

    ans = 10**9
    for i in range(2**D):
        tmp = 0
        cnt = 0
        for j in range(D):
            if (i >> j) & 1:
                tmp += 100 * (j + 1) * pc[j][0] + pc[j][1]
                cnt += pc[j][0]
        if tmp >= G:
            ans = min(ans, cnt)
            continue
        for j in range(D - 1, -1, -1):
            if (i >> j) & 1:
                continue
            for k in range(pc[j][0] - 1):
                tmp += 100 * (j + 1)
                cnt += 1
                if tmp >= G:
                    ans = min(ans, cnt)
        if ans == 10**9:
            ans = cnt
    print(ans)

=======
Suggestion 10

def main():
    # Read a line
    line = input()
    # Split by space
    line = line.split()
    # Convert to int
    D = int(line[0])
    G = int(line[1])
    # Read a line
    line = input()
    # Split by space
    line = line.split()
    # Convert to int
    p = [int(line[i]) for i in range(D)]
    # Read a line
    line = input()
    # Split by space
    line = line.split()
    # Convert to int
    c = [int(line[i]) for i in range(D)]
    # Initialize minimum number of problems
    min_n = 1000
    # Try all combination of problems
    for i in range(2 ** D):
        # Initialize total score
        total_score = 0
        # Initialize number of problems
        n = 0
        # Initialize maximum score
        max_score = 0
        # Try all problems
        for j in range(D):
            # If the j-th problem is solved
            if ((i >> j) & 1) == 1:
                # Add the score to the total score
                total_score += (j + 1) * 100 * p[j] + c[j]
                # Add the number of problems to the total number of problems
                n += p[j]
                # Update the maximum score
                max_score = (j + 1) * 100
        # If the total score is less than the objective
        if total_score < G:
            # Try to solve the problem with the maximum score
            for k in range(p[max_score // 100 - 1]):
                # If the total score is greater than or equal to the objective
                if total_score >= G:
                    # Stop
                    break
                # Add the score to the total score
                total_score += max_score
                # Add the number of problems to the total number of problems
                n += 1
        # If the total score is greater than or equal to the objective
        if total_score >= G:
            # Update the minimum number of problems
            min_n = min(min_n, n)
    # Print the minimum number of problems
    print(min_n)
