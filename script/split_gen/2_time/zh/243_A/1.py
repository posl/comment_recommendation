def main():
    S = input()
    Q = int(input())
    for i in range(Q):
        t, k = map(int, input().split())
        t %= 3
        k -= 1
        if t == 1:
            t = 2
        elif t == 2:
            t = 1
        if k >= len(S):
            k %= len(S)
        print(S[k])
