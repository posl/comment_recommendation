def main():
    N = int(input())
    S = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        a = 1
        while True:
            b = (S[i] - 3*a) / (3 + 4*a)
            if b == int(b) and b > 0:
                break
            a += 1
        if S[i] != 4*a*b + 3*a + 3*b:
            ans += 1
    print(ans)
