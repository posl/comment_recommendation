def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        k -= 1
        while t:
            if S[k] == 'A':
                k = k % (2 ** t)
            elif S[k] == 'B':
                k = (2 ** t) + k % (2 ** t)
            elif S[k] == 'C':
                k = (4 ** t) + k % (2 ** t)
            t -= 1
        print(S[k])
