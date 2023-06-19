def main():
    K = int(input())
    S = [0] * 10
    for i in range(1, 10):
        S[i] = i
    for i in range(1, 10):
        for j in range(1, 10):
            if (i * 10 + j) > 10 ** 15:
                break
            S.append(i * 10 + j)
            if len(S) == K + 1:
                break
    S.sort()
    for i in range(1, K + 1):
        print(S[i])
main()
