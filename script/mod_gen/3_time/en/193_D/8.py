def main():
    K = int(input())
    S = list(input())
    T = list(input())
    rest = 9 * K - 8
    score = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                cnt = K - 2
            else:
                cnt = K - 1
            if cnt < 0:
                continue
            if i == int(S[0]) and j == int(S[1]):
                cnt -= 1
            if i == int(S[2]) and j == int(S[3]):
                cnt -= 1
            if i == int(T[0]) and j == int(T[1]):
                cnt -= 1
            if i == int(T[2]) and j == int(T[3]):
                cnt -= 1
            if cnt < 0:
                continue
            if i == int(S[0]) and j == int(S[1]):
                score += i * 10 ** (cnt + 1)
            elif i == int(S[0]) or j == int(S[1]):
                score += i * 10 ** cnt
            if i == int(S[2]) and j == int(S[3]):
                score += i * 10 ** (cnt + 1)
            elif i == int(S[2]) or j == int(S[3]):
                score += i * 10 ** cnt
            if i == int(T[0]) and j == int(T[1]):
                score += i * 10 ** (cnt + 1)
            elif i == int(T[0]) or j == int(T[1]):
                score += i * 10 ** cnt
            if i == int(T[2]) and j == int(T[3]):
                score += i * 10 ** (cnt + 1)
            elif i == int(T[2]) or j == int(T[3]):
                score += i * 10 ** cnt
    print(score / (rest * (rest - 1)))

if __name__ == '__main__':
    main()