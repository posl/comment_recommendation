def main():
    N = int(input())
    S = list(map(int, input().split()))
    count = 0
    for i in range(N):
        a = 1
        while True:
            b = 1
            while True:
                if 4*a*b + 3*a + 3*b == S[i]:
                    break
                elif 4*a*b + 3*a + 3*b > S[i]:
                    count += 1
                    break
                b += 1
            if 4*a*b + 3*a + 3*b == S[i]:
                break
            a += 1
    print(count)
