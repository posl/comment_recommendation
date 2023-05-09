def main():
    # 入力
    X, N = map(int, input().split())
    p = list(map(int, input().split()))
    # 出力
    if N == 0:
        print(X)
    else:
        p.sort()
        if X <= p[0]:
            print(p[0])
        elif X >= p[-1]:
            print(p[-1])
        else:
            for i in range(N):
                if p[i] <= X and X <= p[i+1]:
                    if abs(p[i]-X) <= abs(p[i+1]-X):
                        print(p[i])
                    else:
                        print(p[i+1])
main()
