def main():
    S = input()
    Q = int(input())
    s = S
    for i in range(Q):
        t, k = map(int, input().split())
        if t == 0:
            s = s[k:] + s[:k]
        else:
            s = s[-k:] + s[:-k]
    print(s)
