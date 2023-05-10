def main():
    N = int(input())
    S = []
    T = []
    for i in range(N):
        s, t = input().split()
        S.append(s)
        T.append(int(t))
    max_score = 0
    max_score_index = 0
    for i in range(N):
        if T[i] > max_score:
            max_score = T[i]
            max_score_index = i
    print(max_score_index + 1)

if __name__ == '__main__':
    main()