def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # 両方とも点数が高い順に並べる
    AB = []
    for i in range(N):
        AB.append({'no': i, 'a': A[i], 'b': B[i]})
    AB.sort(key=lambda x: x['b'], reverse=True)
    AB.sort(key=lambda x: x['a'], reverse=True)
    # 合格者を出力する
    for i in range(X):
        print(AB[i]['no'] + 1)
    for i in range(X, X + Y):
        print(AB[i]['no'] + 1)
    for i in range(X + Y, X + Y + Z):
        print(AB[i]['no'] + 1)
