def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        k -= 1
        for i in range(t, -1, -1):
            if S[k] == 'A':
                pass
            elif S[k] == 'B':
                if i % 3 == 1:
                    k = (k + 1) % len(S)
                elif i % 3 == 2:
                    k = (k - 1) % len(S)
            elif S[k] == 'C':
                if i % 3 == 1:
                    k = (k - 1) % len(S)
                elif i % 3 == 2:
                    k = (k + 1) % len(S)
        print(S[k])
