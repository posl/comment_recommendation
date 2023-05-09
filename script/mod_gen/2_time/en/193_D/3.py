def main():
    K = int(input())
    S = input()
    T = input()
    s = 0
    t = 0
    for i in range(1, 10):
        s += i * 10 ** (S.count(str(i)) + T.count(str(i)))
        t += i * 10 ** (S.count(str(i)) + T.count(str(i)) - 1)
    s -= 10 ** (int(S[-1]) + int(T[-1]))
    t -= 10 ** (int(S[-1]) + int(T[-1]) - 1)
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            if s + i * 10 ** (S.count(str(i)) + T.count(str(i)) - 1) > t + j * 10 ** (S.count(str(j)) + T.count(str(j)) - 1):
                if S.count(str(i)) + T.count(str(i)) < K:
                    ans += (S.count(str(i)) + T.count(str(i)) + 1) * (K - S.count(str(i)) - T.count(str(i))) / (9 * K * (K - 1))
                else:
                    ans += 0
            else:
                ans += 0
    print(ans)

if __name__ == '__main__':
    main()