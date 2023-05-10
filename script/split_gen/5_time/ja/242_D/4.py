def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        t = t % 3
        k = k - 1
        for _ in range(t):
            S = S.replace("A", "BC")
            S = S.replace("B", "CA")
            S = S.replace("C", "AB")
        print(S[k])
