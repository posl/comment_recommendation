def main():
    K = int(input())
    S = input()
    T = input()
    a = [K] * 9
    for i in range(4):
        a[int(S[i]) - 1] -= 1
        a[int(T[i]) - 1] -= 1
    t = 0
    for i in range(9):
        for j in range(9):
            if i == j:
                n = a[i] - 1
                m = a[j] - 1
            else:
                n = a[i] - 1
                m = a[j]
            if n < 0 or m < 0:
                continue
            if (i + 1) * 10 + (j + 1) > (j + 1) * 10 + (i + 1):
                t += n * m
    print(t / (K * (K - 1) * (K - 2) * (K - 3) * (K - 4)))

if __name__ == '__main__':
    main()