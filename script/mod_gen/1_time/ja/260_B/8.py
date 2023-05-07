def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    #数学の点が高い方から X 人を合格とする。
    A1 = sorted(enumerate(A), key=lambda x: x[1], reverse=True)
    A1 = [i[0] for i in A1[:X]]
    #次に、この時点でまだ合格となっていない受験者のうち、英語の点が高い方から Y 人を合格とする。
    B1 = sorted(enumerate(B), key=lambda x: x[1], reverse=True)
    B1 = [i[0] for i in B1[:Y]]
    #次に、この時点でまだ合格となっていない受験者のうち、数学と英語の合計点が高い方から Z 人を合格とする。
    C = [a+b for a, b in zip(A, B)]
    C1 = sorted(enumerate(C), key=lambda x: x[1], reverse=True)
    C1 = [i[0] for i in C1[:Z]]
    #A1, B1, C1の合計を取る
    D = A1 + B1 + C1
    D = sorted(set(D))
    #出力
    for i in D:
        print(i+1)

if __name__ == '__main__':
    main()