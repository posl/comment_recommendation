def main():
    K = int(input())
    S = input()
    T = input()
    S = S[:4]
    T = T[:4]
    S = list(map(int, S))
    T = list(map(int, T))
    win = 0
    for i in range(1, 10):
        for j in range(1, 10):
            if S.count(i) < K and T.count(j) < K:
                S.append(i)
                T.append(j)
                if sum(S) > sum(T):
                    win += (K - S.count(i)) * (K - T.count(j))
                S.pop()
                T.pop()
    total = (9 * K - 8) * (9 * K - 9)
    print(win / total)

if __name__ == '__main__':
    main()