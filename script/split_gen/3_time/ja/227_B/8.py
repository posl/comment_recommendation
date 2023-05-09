def main():
    N = int(input())
    S = list(map(int,input().split()))
    count = 0
    for i in range(N):
        a = 1
        b = 1
        while a*a <= S[i]:
            if S[i] % a == 0:
                b = S[i] // a
                if 4*a*b+3*a+3*b == S[i]:
                    break
            a += 1
        if a*a > S[i]:
            count += 1
    print(count)
