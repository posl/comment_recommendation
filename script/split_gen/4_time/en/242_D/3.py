def main():
    S = input()
    Q = int(input())
    for q in range(Q):
        t, k = map(int, input().split())
        if t == 0:
            print(S[k - 1])
        else:
            if k % len(S) == 0:
                print(S[-1])
            else:
                print(S[k % len(S) - 1])
