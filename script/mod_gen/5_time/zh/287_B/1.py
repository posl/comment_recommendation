def main():
    N, M = map(int, input().split())
    S = []
    for i in range(N):
        S.append(input())
    T = []
    for i in range(M):
        T.append(input())
    count = 0
    for t in T:
        for s in S:
            if t == s[-3:]:
                count += 1
                break
    print(count)

if __name__ == '__main__':
    main()