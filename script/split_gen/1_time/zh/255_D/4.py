def main():
    N,Q = map(int, input().split())
    A = list(map(int, input().split()))
    X = []
    for i in range(Q):
        X.append(int(input()))
    for x in X:
        print(min([abs(a - x) for a in A]))
