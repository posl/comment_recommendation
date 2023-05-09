def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    CD = [list(map(int, input().split())) for i in range(M)]
    # 高橋君のおもちゃのボールを結ぶひもの数
    A = [0] * N
    # 青木君のおもちゃのボールを結ぶひもの数
    C = [0] * N
    for a, b in AB:
        A[a-1] += 1
        A[b-1] += 1
    for c, d in CD:
        C[c-1] += 1
        C[d-1] += 1
    if A == C:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()