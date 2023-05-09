def main():
    K = int(input())
    S = input()
    T = input()
    if K == 1:
        print(0)
        return
    s = [0] * 9
    t = [0] * 9
    for i in range(4):
        s[int(S[i]) - 1] += 1
        t[int(T[i]) - 1] += 1
    p = [K] * 9
    for i in range(9):
        p[i] -= s[i] + t[i]
    ans = 0
    for i in range(9):
        for j in range(9):
            if i == j:
                if p[i] < 2:
                    continue
                s[i] += 1
                t[j] += 1
                p[i] -= 2
            else:
                if p[i] < 1 or p[j] < 1:
                    continue
                s[i] += 1
                t[j] += 1
                p[i] -= 1
                p[j] -= 1
            s_sum = 0
            for k in range(9):
                s_sum += (k + 1) * 10 ** s[k]
            t_sum = 0
            for k in range(9):
                t_sum += (k + 1) * 10 ** t[k]
            if s_sum > t_sum:
                if i == j:
                    ans += p[i] * (p[i] - 1) / ((K - 2) * (K - 1))
                else:
                    ans += p[i] * p[j] / ((K - 2) * (K - 1))
            if i == j:
                s[i] -= 1
                t[j] -= 1
                p[i] += 2
            else:
                s[i] -= 1
                t[j] -= 1
                p[i] += 1
                p[j] += 1
    print(ans)

if __name__ == '__main__':
    main()