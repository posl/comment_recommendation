def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        t %= 3
        if t == 0:
            print(S[(k-1) % len(S)])
        elif t == 1:
            print(S[(k-1) % len(S) + len(S)])
        else:
            print(S[(k-1) % len(S) + 2*len(S)])
