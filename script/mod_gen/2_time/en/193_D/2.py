def main():
    K = int(input())
    S = input()
    T = input()
    T1 = [0] * 10
    T2 = [0] * 10
    for i in range(4):
        T1[int(S[i])] += 1
        T2[int(T[i])] += 1
    T1[9] = 1
    T2[9] = 1
    P1 = [0] * 10
    P2 = [0] * 10
    for i in range(1, 10):
        P1[i] = (K - T1[i]) / (K - i + 1)
        P2[i] = (K - T2[i]) / (K - i + 1)
    #print(P1)
    #print(P2)
    T3 = [0] * 10
    T4 = [0] * 10
    for i in range(1, 10):
        T3[i] = (K - T1[i]) / (K - i + 1)
        T4[i] = (K - T2[i]) / (K - i + 1)
    #print(T3)
    #print(T4)
    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            if sum(T1) + sum(T2) == 9:
                if sum(T1) > sum(T2):
                    ans += P1[i] * P2[j]
                continue
            if i != j:
                if sum(T1) + T1[i] + T2[j] > sum(T2) + T2[j] + T1[i]:
                    ans += P1[i] * P2[j]
    print(ans)

if __name__ == '__main__':
    main()