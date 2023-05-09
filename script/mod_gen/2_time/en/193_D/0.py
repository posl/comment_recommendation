def main():
    K = int(input())
    S = input()
    T = input()
    c = [K]*10
    for i in range(4):
        c[int(S[i])] -= 1
        c[int(T[i])] -= 1
    s = 0
    for i in range(1, 10):
        for j in range(1, 10):
            c[i] -= 1
            c[j] -= 1
            t = 0
            for k in range(1, 10):
                t += k * (10 ** max(c[k], 0))
            if i != j:
                if t > 0:
                    s += c[i] * c[j] * 2
            else:
                if t > 0:
                    s += c[i] * (c[j] - 1)
            c[i] += 1
            c[j] += 1
    print(s / (9 * K * (9 * K - 1)))

if __name__ == '__main__':
    main()