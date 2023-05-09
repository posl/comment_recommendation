def main():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    bonus = []
    for i in range(M):
        bonus.append(list(map(int, input().split())))
    time = T
    for i in range(N-1):
        time -= A[i]
        if time <= 0:
            print('No')
            return
        for j in range(M):
            if i+1 == bonus[j][0]:
                time += bonus[j][1]
    print('Yes')

if __name__ == '__main__':
    main()