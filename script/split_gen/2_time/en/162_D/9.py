def main():
    N = int(input())
    S = input()
    r = 0
    g = 0
    b = 0
    for s in S:
        if s == 'R':
            r += 1
        elif s == 'G':
            g += 1
        elif s == 'B':
            b += 1
    ans = r*g*b
    for i in range(N):
        for j in range(i+1,N):
            k = 2*j - i
            if k >= N:
                continue
            if S[i] == S[j] or S[i] == S[k] or S[j] == S[k]:
                continue
            ans -= 1
    print(ans)
