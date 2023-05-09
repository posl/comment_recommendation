def main():
    X = input()
    N = int(input())
    S = [input() for _ in range(N)]
    dic = {X[i]: i for i in range(26)}
    S.sort(key=lambda x: [dic[x[i]] for i in range(len(x))])
    for s in S:
        print(s)
